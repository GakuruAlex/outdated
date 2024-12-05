from datetime import datetime, date
class Outdated:
    def __init__(self):
        self.formats = [
            "%m/%d/%Y",
            "%B %d, %Y"
        ]
    def get_date_format(self, given_date: str)-> str:
        for format in self.formats:
            try:
                datetime.strptime(given_date, format)
                return format
            except ValueError:
                continue
        
    
    def format_str_to_date(self, given_date: str) -> datetime:
        if self.get_date_format(given_date):
            try:
                new_date = datetime.strptime(given_date,self.get_date_format(given_date))
            except TypeError:
                self.main()
            else:
                return new_date
        return self.main()
    def format_date(self, given_date: str)-> str:
        """_Given a datetime object convert it to YYYY-MM-DD_

        Args:
            given_date (str): _Given date_

        Returns:
            str: _Formatted str date_
        Example:
            >>> format_date("September 8, 1956")
                1956-09-08
        """
        return date.strftime(self.format_str_to_date(given_date), "%Y-%m-%d")
        
    
    def main(self):
        given_date: str = input("Date: ")
        print(f"{self.format_date(given_date.strip())}")   

if __name__ == "__main__":
    outdated = Outdated()
    outdated.main()
    
            