def main():
    countries = ["India", "Italy", "UK", "US", "Chin", "Canada"]
    result = [country for country in countries if 'a' not in country.lower()]
    print(result)  



if __name__ == "__main__":
    main()
    
    