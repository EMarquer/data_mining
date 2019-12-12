import click # Command line library

#import numpy as np
import pandas as pd
from sklearn.externals import joblib
from sklearn import preprocessing

def read_keeped_columns(f):
    """Read the list of columns in a file that to we want to keep in the dataset"""
    
    with open(f,"r") as reader:
        columns = reader.readlines()
    return [col.strip() for col in columns]


# We define a group of commands
@click.group()
def cli():
    pass



@click.option("--preprocessor", default = "le.pickle",help="The location to store the label encoder.")
@click.option("--out", default = "data_out.csv",help="The place to store the result of the spmf encoding.")
@click.argument('columns')
@click.argument('data')
@cli.command()
def encode(data,columns,out,preprocessor):
    """Transform a CSV file into a SPMF table.

    Each multivaluated attributes is transformed into single-valued attributes which are then associated to a number
    and all the attributes on a line are sorted from the lower to the higher value.

      COLUMNS : The path of the file that contains the columns to keep.
      DATA: The csv file.
    """
    
    print("Extraction of the selected columns")
    cols = read_keeped_columns(columns)
    df = pd.read_csv(data,sep=";",usecols = cols)

    print("Multivaluated attributes are now converted into single-valued attributes.")

    # We will build each pair from COLUM_NAME X VALUES 
    content =  df.to_dict(orient = "list")
    binarization = dict()
    for col,vals in content.items():
        binarization[col] = [col+"_"+ str(val) for val in vals]

    print("Labels are now integers.")

    # We fit the label encoder
    binarization = pd.DataFrame(binarization)
    le = preprocessing.LabelEncoder()
    le.fit(binarization.values.flatten())

    print("Export of the encoder and the new table.")

    # We map the strings to integers
    binarization.apply(le.transform).to_csv(out,index=False,header=False,sep=" ")

    # Export Label encoder object
    with open(preprocessor, 'wb') as handler:
        joblib.dump(le,handler)

        
@cli.command()
@click.argument('data')
@click.argument('encoder')
@click.argument('out-decode')
def decode(data,encoder,out_decode):
   """Decode the SPMF output.

     DATA : The SPMF output.
     ENCODER : The place to find the label encoder.
     OUT-DECODER: The smpf decoded output. 
   """

   # We load the label encoder
   print("Loading of the label encoder.")

   with open(encoder,'rb') as handler:
       le = joblib.load(handler)

   # We build a dataframe from the output of spmf 
   df = pd.read_csv(data,sep="#SUP:",names=["itemset","support"])

   print("CSV loaded.")

   # We define a way to convert the itemset (sequence of ints) into the sequence of string. 
   def ints_to_string(int_sequence):
     traduction = []  
     for elem in int_sequence.split():
       if not elem == "==>":
         traduction_elem = le.inverse_transform([int(elem)]) 
         traduction.extend(traduction_elem)
       else:
         traduction.append(elem)
     return " ".join(traduction)

   # We use the previous function to convert the sequences of ints into their corresponding values in the string domain for each cell.

   df["itemset"]=df["itemset"].apply(ints_to_string)
   print(out_decode)

   df.to_csv(out_decode,sep=" ",index=False)
   print("Decoding done.")
   
if __name__ == '__main__':
    cli()
