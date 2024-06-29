def main():
    testDict = {
        "Data A": {"Sub Data A": "valueA"},
        "Data B": {"Sub Data B": "valueB"},
        "Data C": {"Sub Data C": "valueC"},
        "Data D": {"Sub Data D": "valueD"}
    }

    output = {}

    for key, sub_dict in testDict.items():
        for sub_key, value in sub_dict.items():
            output[key] = [[sub_key, value]]

    print(output)

if __name__ == "__main__":
    main()