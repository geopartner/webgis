import json
import glob

# This function reads a json file into an object
def read_json_file(filename):
    with open(filename) as json_file:
        return json.load(json_file)


# This function checks if a file without extension exists in current directory
def check_file_exists(filename):
    return glob.glob(filename + ".*")


# This function finds all json files in current directory
def find_json_files():
    return glob.glob("*.json")


VALID_KOMKODES = [
    "0101",
    "0147",
    "0151",
    "0153",
    "0155",
    "0157",
    "0159",
    "0161",
    "0163",
    "0165",
    "0167",
    "0169",
    "0173",
    "0175",
    "0183",
    "0185",
    "0187",
    "0190",
    "0201",
    "0210",
    "0217",
    "0219",
    "0223",
    "0230",
    "0240",
    "0250",
    "0253",
    "0259",
    "0260",
    "0265",
    "0269",
    "0270",
    "0306",
    "0316",
    "0320",
    "0326",
    "0329",
    "0330",
    "0336",
    "0340",
    "0350",
    "0360",
    "0370",
    "0376",
    "0390",
    "0400",
    "0410",
    "0411",
    "0420",
    "0430",
    "0440",
    "0450",
    "0461",
    "0479",
    "0480",
    "0482",
    "0492",
    "0510",
    "0530",
    "0540",
    "0550",
    "0561",
    "0563",
    "0573",
    "0575",
    "0580",
    "0607",
    "0615",
    "0621",
    "0630",
    "0657",
    "0661",
    "0665",
    "0671",
    "0706",
    "0707",
    "0710",
    "0727",
    "0730",
    "0740",
    "0741",
    "0746",
    "0751",
    "0756",
    "0760",
    "0766",
    "0773",
    "0779",
    "0787",
    "0791",
    "0810",
    "0813",
    "0820",
    "0825",
    "0840",
    "0846",
    "0849",
    "0851",
    "0860",
]


if __name__ == "__main__":

    errs = []
    cfgs = find_json_files()

    try:
        for cfg in cfgs:
            config = read_json_file(cfg)

            # This function adds a line to the error list starting with the configuration file name
            def add_error(error):
                errs.append("{}: {}".format(cfg, error))

            # Check if print configuration exists
            if "enabledPrints" in config:
                for print in config["enabledPrints"]:
                    if not check_file_exists(print):
                        add_error("Print configuration {} does not exist".format(print))

            # Check if kommunekodes are valid
            if "searchConfig" in config and "komkode" in config["searchConfig"]:
                for komkode in config["searchConfig"]["komkode"]:
                    if komkode in VALID_KOMKODES:
                        add_error("Kommunekode {} does not exist".format(komkode))

        # Print all errors
        for err in errs:
            print("")
            print(err)

    except Exception as e:
        print("Error: {}".format(e))
