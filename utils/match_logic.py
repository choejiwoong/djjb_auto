import datetime
import re


def parse_pos(val) -> int | None:
    """위치값 파싱: '13K020' → 13020, '9150' → 9150, 그 외 → None"""
    if val is None:
        return None
    s = str(val).strip()
    m = re.match(r'^(\d+)[Kk](\d+)$', s)
    if m:
        return int(m.group(1)) * 1000 + int(m.group(2))
    if re.match(r'^\d+(\.\d+)?$', s):
        return int(float(s))
    return None


def overlaps(a0, a1, b0, b1) -> bool:
    """두 구간이 겹치는지 확인"""
    if any(v is None for v in (a0, a1, b0, b1)):
        return False
    return max(min(a0, a1), min(b0, b1)) <= min(max(a0, a1), max(b0, b1))


def load_perf(ws) -> tuple[str, str, list[dict]]:
    """
    파일2 '장비별 세부작업실적' 시트 파싱.
    반환: (1호명, 2호명, 실적레코드 리스트)
    """
    car1 = str(ws['C4'].value or '1호 레일연마차')
    car2 = str(ws['K4'].value or '2호 레일연마차')
    records = []

    for row in ws.iter_rows(min_row=7, values_only=True):
        # 1호: C(2)=일자, E(4)=구간, F(5)=부터, G(6)=까지
        # 2호: K(10)=일자, M(12)=구간, N(13)=부터, O(14)=까지
        for car_name, di, seg_i, fi, ti in [
            (car1, 2, 4, 5, 6),
            (car2, 10, 12, 13, 14),
        ]:
            d = row[di]
            if d is None or not isinstance(d, (int, float)):
                continue
            fr, to, seg = row[fi], row[ti], row[seg_i]
            records.append({
                'car':      car_name,
                'day':      int(d),
                'segment':  str(seg) if seg is not None else '-',
                'from_raw': fr,
                'to_raw':   to,
                'from_m':   parse_pos(fr),
                'to_m':     parse_pos(to),
            })

    return car1, car2, records


def run_match(ws1, perf_records: list[dict], year: int, month: int) -> tuple[list, list]:
    """
    파일1 구간 시트와 실적 레코드를 비교해 매칭/미매칭 목록 반환.
    반환: (matched 리스트, unmatched 리스트)
    """
    results, unmatched = [], []
    current_date = None
    last_start = last_end = last_b = last_c = last_d = None

    for row in ws1.iter_rows(min_row=7, values_only=True):
        a, b, c, d, e, f = row[0], row[1], row[2], row[3], row[4], row[5]
        i_val = row[8]

        # 날짜 갱신
        if isinstance(a, datetime.datetime):
            current_date = a
        elif isinstance(a, str):
            m = re.match(r'(\d+)/(\d+)', a)
            if m:
                try:
                    current_date = datetime.datetime(year, int(m.group(1)), int(m.group(2)))
                except ValueError:
                    pass

        if current_date is None:
            continue

        # 시점/종점 forward-fill
        if b:
            last_b, last_c, last_d = b, c, d
            last_start, last_end = e, f
        elif e:
            last_start = e
            last_end = f if f else last_end

        # 공종 필터
        if not i_val or '레일연마' not in str(i_val):
            continue

        use_start = e if e is not None else last_start
        use_end   = f if f is not None else last_end
        start_m   = parse_pos(use_start)
        end_m     = parse_pos(use_end)
        day       = current_date.day

        matched = False
        for p in perf_records:
            if p['day'] != day:
                continue
            if overlaps(start_m, end_m, p['from_m'], p['to_m']):
                matched = True
                results.append({
                    '일자':      current_date.strftime('%Y. %m. %d.'),
                    '연마차명':  p['car'],
                    '공종':      str(i_val),
                    '분소':      str(last_b or '-'),
                    '일정_시점': str(use_start) if use_start is not None else '-',
                    '일정_종점': str(use_end)   if use_end   is not None else '-',
                    '실적_구간': p['segment'],
                    '실적_부터': str(p['from_raw']),
                    '실적_까지': str(p['to_raw']),
                })

        if not matched and (start_m or end_m):
            unmatched.append({
                '일자':      current_date.strftime('%Y. %m. %d.'),
                '공종':      str(i_val),
                '분소':      str(last_b or '-'),
                '일정_시점': str(use_start) if use_start is not None else '-',
                '일정_종점': str(use_end)   if use_end   is not None else '-',
                '사유':      '해당 날짜 실적에 겹치는 구간 없음',
            })

    return results, unmatched


def extract_year_month(filename: str) -> tuple[int, int]:
    """파일명에서 연도·월 자동 추출. 예: '2026년_5월_...' → (2026, 5)"""
    m = re.search(r'(\d{4})년.?(\d{1,2})월', filename)
    if m:
        return int(m.group(1)), int(m.group(2))
    import datetime as dt
    now = dt.datetime.now()
    return now.year, now.month
