#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import click



    

def read_attributes(f):
    """Read a list of attributes in a file"""
    with open(f,"r") as reader:
        attrs = reader.readlines()
    return [attr.strip() for attr in attrs]

# Retrieve the 2 set of attributes (one for the housing part and the other for person)
PERSON_ATTR = read_attributes("person.txt")
HOUSING_ATTR = read_attributes("housing.txt")


def is_an_interesting_rule(rule):
    """Criterium to decide if the rule is interesting:

    - at least one person attribute on the left hand side of the rule
    - at least one housing attribute on the right hand side.
    
    """
    valid_l_hand_side = any([attr in rule['left_hand_side'] for attr in PERSON_ATTR])
    valid_r_hand_side = any([attr in rule['right_hand_side'] for attr in HOUSING_ATTR])
    return valid_l_hand_side and valid_r_hand_side



@click.command()
@click.argument('rules')
@click.argument('rules_out')
def main(rules,rules_out):
    """ Take a csv of rules and returns the rule that we want to select """
    
    df = pd.read_csv(rules,sep=" ",usecols=["itemset"])
    df['rules'] = df['itemset'].apply(lambda x: x.split("==>"))
    rules_df = pd.DataFrame()

    # Split the rules by left and right hand side
    rules_df["left_hand_side"] = df['rules'].apply(lambda x: x[0])
    rules_df["right_hand_side"] = df['rules'].apply(lambda x: x[1])

    # Matching rules
    rules_df["valid"] = rules_df.apply(is_an_interesting_rule,axis=1)
    selected_rules=rules_df[rules_df["valid"]==True].sort_values(by=['right_hand_side'])

    # Export
    selected_rules.to_csv(rules_out,columns=['left_hand_side','right_hand_side'],sep=">",header=False,index=False)
    print("Selection of rules in {} done.".format(rules))

if __name__ == "__main__":
    main()


