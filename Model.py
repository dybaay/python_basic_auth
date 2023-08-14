from dbConnect import conn, cursor


class Model:

    @staticmethod
    def create(data: dict):

        if data:
            fields = ", ".join(data.keys())
            placeholders = ", ".join(["%s"] * len(data))
            query = f"INSERT INTO users({fields}) VALUES ({placeholders})"
            values = tuple(data.values())

            try:
                cursor.execute(query, values)
                conn.commit()
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                pass