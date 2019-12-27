# Practical Work: Itemsets and Association Rules Mining
Class project under the supervision of Yannick Toussaint for the Data Mining class.

Realized by Maxime Guillaume and Esteban Marquer.

## Outline
- [Outline](#outline)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Files](#files)
- [Report](./Report.pdf) (external file)

## Dependencies
This project was realized using SPMF v2.39, you will need a working Java installation to use the software.

To run the utility scripts you will need Python 3.7 with the following libraries:
- `click` (version 7 or more recent): a command line interface (CLI) library;
- `pandas` (version 0.25 or more recent): a data handling library;
- `sklearn` (version 0.21 or more recent): a machine learning and data processing library;
- `pickle` (should be provided with Python 3.7): an object serialization library.

To run the Bash scripts (`.sh` files) used in the project, use linux system or any Bash interpreter accepting the following Bash commands:
- `python`;
- `wc`;
- `mkdir`;
- `sort`;
- `uniq`;
- `echo`.

## Usage
The following section describes the recomended way to use the project.

### Setup
To setup the project you will need to:
- install Python and the dependencies (see [Dependencies](#dependencies));
- put the corpus at the root of the repository, in a file named `GrandEst`, without extension, and preprocess it following [Preprocessing](#preprocessing); an alternative is to unzip the provided preprocessed file in [`binary_grand_est.csv.zip`](./binary_grand_est.csv.zip) to the root of the repository.
- check that SPMF works by running the [`spmf.jar`](./spmf.jar) JAR file with Java.

### Preprocessing
If you wish to preprocess the corpus or use an other version of the corpus, you will need to run the [`Src/encode.sh`](./Src/encode.sh) script from the root of the repository.

An alternative is to unzip the provided preprocessed file in [`binary_grand_est.csv.zip`](./binary_grand_est.csv.zip) to the root of the repository, under the name `binary_grand_est.csv`.

### Itemset Extraction
To perform the itemset extraction, we recommend to follow the steps described in this section.

1. Start SPMF and run the FPGrown algorithm for itemset extraction on the `binary_grand_est.csv` file. We recommend to run the algorithm with `min_sup` equal to 40%, 50%, 60%, 70%, 80% and 90%. Save the output in the [`Patterns`](./Patterns) folder under `FPG_<min support (in %)>.txt` (replace `<min support (in %)>` by the value of `min_sup`, without the `%` symbol).
2. **[optional]** You can also run the FPClosed algorithm for itemset extraction on the `binary_grand_est.csv` file, using SPMF. Save the output in the [`Patterns`](./Patterns) folder under `FPC_<min support (in %)>.txt` (replace `<min support (in %)>` by the value of `min_sup`, without the `%` symbol).
3. Run [`Src/decode_itemsets.sh`](./Src/decode_itemsets.sh) from the root of the repository to decode the output files in the [`Patterns`](./Patterns) folder and store the output in [`DecodedPatterns`](./DecodedPatterns).
4. Run [`Src/count_item.sh`](./Src/count_item.sh) from the root of the repository to count the number of itemsets in each file of the [`Patterns`](./Patterns) folder.
5. **[optional]** If you ran FPGrown with `min_sup` equal to 40%, 50%, 60%, 70%, 80% and 90%, you can run [`Src/diff.sh`](./Src/diff.sh) to group the decoded outputs in slices of 10% of support.

Once all the steps are performed, you can manually analyse the results.

### Association Rule Extraction
To perform the association rule extraction, we recommend to follow the steps described in this section.

1. Start SPMF and run the FPGrown algorithm for association rule extraction on the `binary_grand_est.csv` file. We recommend to run the algorithm with various values for `min_sup` and `min_conf`. Save the output in the [`Rules`](./Rules) folder under `FPG_<min support (in %)>_<min confidence (in %)>.txt` (replace `<min support (in %)>` by the value of `min_sup` and `<min confidence (in %)>` with the value of `min_conf`, without the `%` symbol).
2. Run [`Src/decode_rules.sh`](./Src/decode_rules.sh) from the root of the repository to decode the output files in the [`Rules`](./Rules) folder and store the output in [`DecodedRules`](./DecodedRules).
run spmf, save output in [`Rules`](./Rules)
3. Run [`Src/count_rules.sh`](./Src/count_rules.sh) from the root of the repository to count the number of association rules in each file of the [`Rules`](./Rules) folder.
3. Run [`Src/filter_rules.sh`](./Src/filter_rules.sh) from the root of the repository to filter the association rules in each file of the [`DecodedRules`](./DecodedRules) folder, as described in the report. The output is stored in the [`FilteredRules`](./FilteredRules) folder. This process relies on the [`housing.txt`](./housing.txt) and [`person.txt`](./person.txt) files.

Once all the steps are performed, you can manually analyse the results.

## Files
### Output Folders for Itemset Extraction
- [`Patterns`](./Patterns): folder containing the encoded patterns (frequent itemsets) extracted using the FPClosed and the FPGrown algorithms with different values for the `min_sup`. Those files corresponds to the raw outputs of SPMF. Each file name correspond to `<algorithm>_<min support (in %)>.txt`.
- [`DecodedPatterns`](./DecodedPatterns): folder containing the decoded patterns (frequent itemsets) extracted using the FPGrown algorithm with different values for the `min_sup`. Each file name correspond to `<algorithm>_<min support (in %)>.txt`.
- [`DecodedPatterns/Diff`](./DecodedPatterns/Diff): folder containing the patterns (frequent itemsets) extracted using the FPGrown algorithm, groupped by slices of support. Each file name correspond to `<algorithm>_<min support (in %)>_<max support (in %)>.txt`.

### Output Folders for Association Rule Extraction
- [`Rules`](./Rules): folder containing the encoded association rules extracted using the FPGrown algorithm with different values for the `min_sup` and the `min_conf`. Those files corresponds to the raw outputs of SPMF. Each file name correspond to `<algorithm>_<min support (in %)>_<min confidence (in %)>.txt`.
- [`DecodedRules`](./DecodedRules): folder containing the decoded association rules extracted using the FPGrown algorithm with different values for the `min_sup` and the `min_conf`. Each file name correspond to `<algorithm>_<min support (in %)>_<min confidence (in %)>.txt`.
- [`FilteredRules`](./FilteredRules): folder containing a subset of the decoded association rules extracted using the FPGrown algorithm, with only rules deemed "interesting" for our analysis (see more in the report). Each file name correspond to `<algorithm>_<min support (in %)>_<min confidence (in %)>.txt`.

### Sources and Scripts ([`Src`](./Src) folder)
The recommended use of the scripts is to use the launching Bash scripts from the root of the repository.

- [`Src/filter_rules.py`](./Src/filter_rules.py): Python script to filter the rules deemed "interesting" for our analysis (see more in the report) in a single file. Run `python Src/filter_rules.py --help` for more information. This process relies on the [`housing.txt`](./housing.txt) and [`person.txt`](./person.txt) files.
- [`Src/spmf_encoding.py`](./Src/spmf_encoding.py): Python scripts to encode and decode data (see more in the report). Run `python Src/spmf_encoding.py --help` for more information.


- [`Src/count_item.sh`](./Src/count_item.sh): pure Bash script to enumerate the number of itemsets in the [`Patterns`](./Patterns) folder.
- [`Src/count_rules.sh`](./Src/count_rules.sh): pure Bash script to enumerate the number of association rules in the [`Rules`](./Rules) folder.

- [`Src/decode_itemsets.sh`](./Src/decode_itemsets.sh): launching script for the decoding tool in [`Src/spmf_encoding.py`](./Src/filter_rules.py), applying it on every file in [`Patterns`](./Patterns) and outputing in [`DecodedPatterns`](./DecodedPatterns).
- [`Src/decode_rules.sh`](./Src/decode_rules.sh): launching script for the decoding tool in [`Src/spmf_encoding.py`](./Src/filter_rules.py), applying it on every file in [`Rules`](./Rules) and outputing in [`DecodedRules`](./DecodedRules).

- [`Src/diff.sh`](./Src/diff.sh): pure Bash script to group the itemsets in the [`DecodedPatterns`](./DecodedPatterns) folder by slices of support and outputing in [`DecodedPatterns/Diff`](./DecodedPatterns/Diff).

- [`Src/filter_rules.sh`](./Src/filter_rules.sh): launching script for the [`Src/filter_rules.py`](./Src/filter_rules.py) script on every file in [`DecodedRules/`](./DecodedRules).

- [`Src/encode.sh`](./Src/encode.sh): launching script for the encoding tool in [`Src/spmf_encoding.py`](./Src/filter_rules.py), applying it on every file in [`GrandEst`](./GrandEst) and outputing the `binary_grand_est.csv` file (currently archived in [`binary_grand_est.csv.zip`](./binary_grand_est.csv.zip)).

### Other Files

- `GrandEst` (not present in the repository): CSV file of the corpus, with `;` separator.

- [`binary_grand_est.csv.zip`](./binary_grand_est.csv.zip): archive containing the encoded, binarized and column-filtered corpus.

- [`columns.txt`](./columns.txt): file containing all the column names of the columns to keep during the preprocessing.
- [`housing.txt`](./housing.txt): file containing the subset of the column names in [`columns.txt`](./columns.txt) corresponding to the housing.
- [`person.txt`](./person.txt): file containing the subset of the column names in [`columns.txt`](./columns.txt) corresponding to the socio-economic situation.

- [`le.pickle`](./le.pickle): pickled label encoder from `sklearn`, created by the encoding script and used to decode the outputs from SPMF.

- [`Report.pdf`](./Report.pdf): a report describing the implementation choices and answering the questions from the instruction sheet.
- [`SignificationDesVariables.pdf`](./SignificationDesVariables.pdf): (in French) PDF file describing the various fields in the data.