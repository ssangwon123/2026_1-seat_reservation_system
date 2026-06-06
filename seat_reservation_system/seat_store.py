class SeatStore:
    def __init__(self, seat_ids):
        self._seats = {seat_id: None for seat_id in seat_ids}

    def list_seats(self):
        return self._seats.items()

    def reserve(self, seat_id, name):
        current = self._get(seat_id)
        if current is not None:
            raise ValueError("Seat is already reserved.")
        self._seats[seat_id] = name
        return seat_id, name

    def cancel(self, seat_id, name=None):
        current = self._get(seat_id)
        if current is None:
            raise ValueError("Seat is not reserved.")
        if name and current != name:
            raise ValueError("Name does not match the reservation.")
        self._seats[seat_id] = None
        return seat_id, None

    def status(self, seat_id):
        return seat_id, self._get(seat_id)

    def stats(self):
        reserved = sum(1 for name in self._seats.values() if name)
        total = len(self._seats)
        return {"total": total, "reserved": reserved, "available": total - reserved}
    # 예약자 이름(또는 일부 문자열)으로 예약된 좌석 검색
    def find_reservations_by_name(self, keyword):
        """Find reserved seats whose reserver name contains the given keyword."""
        # 대소문자 구분 없이 검색하기 위해 소문자로 변환
        normalized_keyword = keyword.strip().lower()

        if not normalized_keyword:
            return []

        matched_reservations = []

        for seat_id, reserved_name in self._seats.items():
            if reserved_name is None:
                continue

            if normalized_keyword in reserved_name.lower():
                matched_reservations.append((seat_id, reserved_name))

        return matched_reservations

    def _get(self, seat_id):
        if seat_id not in self._seats:
            raise ValueError("Seat does not exist.")
        return self._seats[seat_id]
