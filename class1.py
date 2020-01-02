import pandas as pd
import ingredients
import streamlit as st
from PIL import Image

data = ingredients.data
fraction = Image.open('fractions.png')
## Turn into a data frame
df = pd.DataFrame(data).transpose()

class baking:
    def __init__(self, ingr, amount, measurement, need):
        ''' I need to write a new one of these. For now: Ta-dah! My class'''
        self.ingr = ingr
        self.amount = amount
        self.measurement = measurement
        self.need = need
        grm = [df.loc[i, 'grams'] for i in df.index if i == ingr]
        self.grm = grm[0]
        ouz = [df.loc[i, 'ounces'] for i in df.index if i == ingr]
        self.ouz = ouz[0]

        if self.measurement == 'gram':
            if need == 'cup':
                cup = round(self.amount/self.grm, ndigits=2)
                if cup <= 1:
                    st.write('{} grams {} is {} cup'.format(self.amount, self.ingr, cup))
                elif self.amount == 1:
                    st.write('{} gram {} is {} cups'.format(self.amount, self.ingr, cup))
                else:
                    st.write('{} grams {} is {} cups'.format(self.amount, self.ingr, cup))
            if need == 'ounce':
                ounce = round(self.amount/(self.grm/self.ouz), ndigits=2)
                if ounce <= 1:
                    st.write('{} grams {} is {} ounce'.format(self.amount, self.ingr, ounce))
                elif self.amount == 1:
                    st.write('{} gram {} is {} ounces'.format(self.amount, self.ingr, ounce))
                else:
                    st.write('{} grams {} is {} ounces'.format(self.amount, self.ingr, ounce))
            if need == 'milliliter':
                ml = round((self.amount/self.grm)*236.588, ndigits=2)
                if ml <= 1:
                    st.write('{} grams {} is {} milliliter'.format(self.amount, self.ingr, ml))
                elif self.amount == 1:
                    st.write('{} gram {} is {} milliliters'.format(self.amount, self.ingr, ml))
                else:
                    st.write('{} grams {} is {} milliliters'.format(self.amount, self.ingr, ml))
            if need == 'gram':
                st.write('Whoops! You chose the same unit of measure that you already have. Try something else!')
            if need == 'teaspoon':
                tsp = round((self.amount/self.grm)*48, ndigits=2)
                if self.amount == 1:
                    st.write('{} gram {} is {} teaspoons'.format(self.amount, self.ingr, tsp))
                elif tsp <= 1:
                    st.write('{} grams {} is {} teaspoon'.format(self.amount, self.ingr, tsp))
                else:
                    st.write('{} grams {} is {} teaspoons'.format(self.amount, self.ingr, tsp))            
            if need == 'tablespoon':
                tbsp = round((self.amount/self.grm)*16, ndigits=2)
                if self.amount == 1:
                    st.write('{} gram {} is {} tablespoons'.format(self.amount, self.ingr, tbsp))
                elif tbsp <= 1:
                    st.write('{} grams {} is {} tablespoon'.format(self.amount, self.ingr, tbsp))
                else:
                    st.write('{} grams {} is {} tablespoons'.format(self.amount, self.ingr, tbsp))  
            if need == 'pound':
                lb = round((self.amount/(self.grm/self.ouz))/16, ndigits=2)
                if lb <= 1:
                    st.write('{} grams {} is {} pound'.format(self.amount, self.ingr, lb))
                elif self.amount == 1:
                    st.write('{} gram {} is {} pounds'.format(self.amount, self.ingr, lb))
                else:
                    st.write('{} grams {} is {} pounds'.format(self.amount, self.ingr, lb))
            if need == 'liter':
                l = round((self.amount/self.grm)*0.236588, ndigits=2)
                if l <= 1:
                    st.write('{} grams {} is {} liter'.format(self.amount, self.ingr, l))
                elif self.amount == 1:
                    st.write('{} gram {} is {} liters'.format(self.amount, self.ingr, l))
                else:
                    st.write('{} grams {} is {} liters'.format(self.amount, self.ingr, l))
            if need == 'fluid ounce':
                floz = round((self.amount/self.grm)*8, ndigits=2)
                if floz <= 1:
                    st.write('{} grams {} is {} fluid ounce'.format(self.amount, self.ingr, floz))
                elif self.amount == 1:
                    st.write('{} gram {} is {} fluid ounces'.format(self.amount, self.ingr, floz))
                else:
                    st.write('{} grams {} is {} fluid ounces'.format(self.amount, self.ingr, floz))
        elif self.measurement == 'cup':
            if need == 'gram':
                gram = round(self.amount*self.grm, ndigits=2)
                if self.amount == 1:
                    st.write('{} cup {} is {} grams'.format(self.amount, self.ingr, gram))
                elif gram <= 1:
                    st.write('{} cups {} is {} gram'.format(self.amount, self.ingr, gram))
                else:
                    st.write('{} cups {} is {} grams'.format(self.amount, self.ingr, gram))
            if need == 'cup':
                st.write('Whoops! You chose the same unit of measure that you already have. Try something else!')
            if need == 'ounce':
                ounce = round(self.amount*self.ouz, ndigits=2)
                if self.amount == 1:
                    st.write('{} cup {} is {} ounce'.format(self.amount, self.ingr, ounce))
                elif ounce <= 1:
                    st.write('{} cups {} is {} ounces'.format(self.amount, self.ingr, ounce))
                else:
                    st.write('{} cups {} is {} ounces'.format(self.amount, self.ingr, ounce))
            if need == 'milliliter':
                ml = round(self.amount*236.588, ndigits=2)
                if self.amount == 1:
                    st.write('{} cup {} is {} milliliters'.format(self.amount, self.ingr, ml))
                elif ml <= 1:
                    st.write('{} cups {} is {} milliliter'.format(self.amount, self.ingr, ml))
                else:
                    st.write('{} cups {} is {} milliliters'.format(self.amount, self.ingr, ml))
            if need == 'teaspoon':
                tsp = round(self.amount*48, ndigits=2)
                if self.amount == 1:
                    st.write('{} cup {} is {} teaspoons'.format(self.amount, self.ingr, tsp))
                elif tsp <= 1:
                    st.write('{} cups {} is {} teaspoon'.format(self.amount, self.ingr, tsp))
                else:
                    st.write('{} cups {} is {} teaspoons'.format(self.amount, self.ingr, tsp))    
            if need == 'tablespoon':
                tbsp = round(self.amount*16, ndigits=2)
                if self.amount == 1:
                    st.write('{} cup {} is {} tablespoons'.format(self.amount, self.ingr, tbsp))
                elif tbsp <= 1:
                    st.write('{} cups {} is {} tablespoon'.format(self.amount, self.ingr, tbsp))
                else:
                    st.write('{} cups {} is {} tablespoons'.format(self.amount, self.ingr, tbsp))
            if need == 'pound':
                lb = round((self.amount*self.ouz)/16, ndigits=2)
                if self.amount == 1:
                    st.write('{} cup {} is {} pounds'.format(self.amount, self.ingr, lb))
                elif lb <= 1:
                    st.write('{} cups {} is {} pound'.format(self.amount, self.ingr, lb))
                else:
                    st.write('{} cups {} is {} pounds'.format(self.amount, self.ingr, lb))
            if need == 'liter':
                l = round(self.amount*0.236588, ndigits=2)
                if self.amount == 1:
                    st.write('{} cup {} is {} liters'.format(self.amount, self.ingr, l))
                elif l <= 1:
                    st.write('{} cups {} is {} liter'.format(self.amount, self.ingr, l))
                else:
                    st.write('{} cups {} is {} liters'.format(self.amount, self.ingr, l))
            if need == 'fluid ounce':
                floz = round(self.amount*8, ndigits=2)
                if self.amount == 1:
                    st.write('{} cup {} is {} fluid ounces'.format(self.amount, self.ingr, floz))
                elif floz <= 1:
                    st.write('{} cups {} is {} fluid ounce'.format(self.amount, self.ingr, floz))
                else:
                    st.write('{} cups {} is {} fluid ounces'.format(self.amount, self.ingr, floz))
        elif self.measurement == 'ounce':
            if need == 'gram':
                gram = round(amount/(self.ouz/self.grm), ndigits=2)
                if self.amount == 1:
                    st.write('{} ounce {} is {} grams'.format(self.amount, self.ingr, gram))
                elif gram <= 1:
                    st.write('{} ounces {} is {} gram'.format(self.amount, self.ingr, gram))
                else:
                    st.write('{} ounces {} is {} grams'.format(self.amount, self.ingr, gram))
            if need == 'cup':
                cup = round(self.amount/self.ouz, ndigits=2)
                if self.amount == 1:
                    st.write('{} ounce {} is {} cups'.format(self.amount, self.ingr, cup))
                elif cup <= 1:
                    st.write('{} ounces {} is {} cup'.format(self.amount, self.ingr, cup))
                else:
                    st.write('{} ounces {} is {} cups'.format(self.amount, self.ingr, cup))
            if need == 'ounce':
                st.write('Whoops! You chose the same unit of measure that you already have. Try something else!')
            if need == 'milliliter':
                ml = round((self.amount/self.ouz)*236.588, ndigits=2)
                if self.amount == 1:
                    st.write('{} ounce {} is {} milliliters'.format(self.amount, self.ingr, ml))
                elif ml <= 1:
                    st.write('{} ounces {} is {} milliliter'.format(self.amount, self.ingr, ml))
                else:
                    st.write('{} ounces {} is {} milliliters'.format(self.amount, self.ingr, ml))
            if need == 'teaspoon':
                tsp = round((self.amount/self.ouz)*48, ndigits=2)
                if self.amount == 1:
                    st.write('{} ounce {} is {} teaspoons'.format(self.amount, self.ingr, tsp))
                elif tsp <= 1:
                    st.write('{} ounces {} is {} teaspoon'.format(self.amount, self.ingr, tsp))
                else:
                    st.write('{} ounces {} is {} teaspoons'.format(self.amount, self.ingr, tsp))
            if need == 'tablespoon':
                tbsp = round((self.amount/self.ouz)*16, ndigits=2)
                if self.amount == 1:
                    st.write('{} ounce {} is {} tablespoons'.format(self.amount, self.ingr, tbsp))
                elif tbsp <= 1:
                    st.write('{} ounces {} is {} tablespoon'.format(self.amount, self.ingr, tbsp))
                else:
                    st.write('{} ounces {} is {} tablespoons'.format(self.amount, self.ingr, tbsp))
            if need == 'pound':
                lb = round(self.amount/16, ndigits=2)
                if self.amount == 1:
                    st.write('{} ounce {} is {} pounds'.format(self.amount, self.ingr, lb))
                elif lb <= 1:
                    st.write('{} ounces {} is {} pound'.format(self.amount, self.ingr, lb))
                else:
                    st.write('{} ounces {} is {} pounds'.format(self.amount, self.ingr, lb))
            if need == 'liter':
                l = round((self.amount/self.ouz)*0.236588, ndigits=2)
                if self.amount == 1:
                    st.write('{} ounce {} is {} liters'.format(self.amount, self.ingr, l))
                elif l <= 1:
                    st.write('{} ounces {} is {} liter'.format(self.amount, self.ingr, l))
                else:
                    st.write('{} ounces {} is {} liters'.format(self.amount, self.ingr, l))
            if need == 'fluid ounce':
                floz = round((self.amount*self.ouz)/8, ndigits=2)
                if self.amount == 1:
                    st.write('{} ounce {} is {} fluid ounces'.format(self.amount, self.ingr, floz))
                elif floz <= 1:
                    st.write('{} ounces {} is {} fluid ounce'.format(self.amount, self.ingr, floz))
                else:
                    st.write('{} ounces {} is {} fluid ounces'.format(self.amount, self.ingr, floz))
        elif self.measurement == 'teaspoon':
            if need == 'gram':
                gram = round((self.amount/48)*self.grm, ndigits=2)
                if self.amount == 1:
                    st.write('{} teaspoon {} is {} grams'.format(self.amount, self.ingr, gram))
                elif gram <= 1:
                    st.write('{} teaspoons {} is {} gram'.format(self.amount, self.ingr, gram))
                else:
                    st.write('{} teaspoons {} is {} grams'.format(self.amount, self.ingr, gram))
            if need == 'cup':
                cup = round((self.amount/48), ndigits=2)
                if self.amount == 1:
                    st.write('{} teaspoon {} is {} cups'.format(self.amount, self.ingr, cup))
                elif cup <= 1:
                    st.write('{} teaspoons {} is {} cup'.format(self.amount, self.ingr, cup))
                else:
                    st.write('{} teaspoons {} is {} cups'.format(self.amount, self.ingr, cup))
            if need == 'ounce':
                ounce = round((self.amount/48)*self.ouz, ndigits=2)
                if self.amount == 1:
                    st.write('{} teaspoon {} is {} ounces'.format(self.amount, self.ingr, ounce))
                elif ounce <= 1:
                    st.write('{} teaspoons {} is {} ounce'.format(self.amount, self.ingr, ounce))
                else:
                    st.write('{} teaspoons {} is {} ounces'.format(self.amount, self.ingr, ounce))
            if need == 'milliliter':
                ml = round((self.amount*4.92892), ndigits=2)
                if self.amount == 1:
                    st.write('{} teaspoon {} is {} milliliters'.format(self.amount, self.ingr, ml))
                elif ml <= 1:
                    st.write('{} teaspoon {} is {} milliliters'.format(self.amount, self.ingr, ml))
                else:
                    st.write('{} teaspoons {} is {} milliliters'.format(self.amount, self.ingr, ml))
            if need == 'teaspoon':
                st.write('Whoops! You chose the same unit of measure that you already have. Try something else!')
            if need == 'tablespoon':
                tbsp = round((self.amount/3), ndigits=2)
                if tbsp <= 1:
                    st.write('{} teaspoons {} is {} tablespoon'.format(self.amount, self.ingr, tbsp))
                elif self.amount == 1:
                    st.write('{} teaspoon {} is {} tablespoons'.format(self.amount, self.ingr, tbsp))
                else:
                    st.write('{} teaspoons {} is {} tablespoons'.format(self.amount, self.ingr, tbsp))
            if need == 'pound':
                lb = round(((self.amount/48)*self.ouz)/16, ndigits=2)
                if self.amount == 1:
                    st.write('{} teaspoon {} is {} pounds'.format(self.amount, self.ingr, lb))
                elif lb <= 1:
                    st.write('{} teaspoons {} is {} pound'.format(self.amount, self.ingr, lb))
                else:
                    st.write('{} teaspoons {} is {} pounds'.format(self.amount, self.ingr, lb))
            if need == 'liter':
                l = round((self.amount*0.00492892), ndigits=2)
                if self.amount == 1:
                    st.write('{} teaspoon {} is {} liters'.format(self.amount, self.ingr, l))
                elif l <= 1:
                    st.write('{} teaspoon {} is {} liters'.format(self.amount, self.ingr, l))
                else:
                    st.write('{} teaspoons {} is {} liters'.format(self.amount, self.ingr, l))
            if need == 'fluid ounce':
                floz = round((self.amount/6), ndigits=2)
                if self.amount == 1:
                    st.write('{} teaspoon {} is {} fluid ounces'.format(self.amount, self.ingr, floz))
                elif floz <= 1:
                    st.write('{} teaspoons {} is {} fluid ounce'.format(self.amount, self.ingr, floz))
                else:
                    st.write('{} teaspoons {} is {} fluid ounces'.format(self.amount, self.ingr, floz))
        elif self.measurement == 'tablespoon':
            if need == 'gram':
                gram = round((self.amount/16)*self.grm, ndigits=2)
                if self.amount == 1:
                    st.write('{} tablespoon {} is {} grams'.format(self.amount, self.ingr, gram))
                elif gram <= 1:
                    st.write('{} tablespoons {} is {} gram'.format(self.amount, self.ingr, gram))
                else:
                    st.write('{} tablespoons {} is {} grams'.format(self.amount, self.ingr, gram))
            if need == 'cup':
                cup = round((self.amount/16), ndigits=2)
                if self.amount == 1:
                    st.write('{} tablespoon {} is {} cups'.format(self.amount, self.ingr, cup))
                elif cup <= 1:
                    st.write('{} tablespoons {} is {} cup'.format(self.amount, self.ingr, cup))
                else:
                    st.write('{} tablespoons {} is {} cups'.format(self.amount, self.ingr, cup))
            if need == 'ounce':
                ounce = round((self.amount/16)*self.ouz, ndigits=2)
                if self.amount == 1:
                    st.write('{} tablespoon {} is {} ounces'.format(self.amount, self.ingr, ounce))
                elif ounce <= 1:
                    st.write('{} tablespoons {} is {} ounce'.format(self.amount, self.ingr, ounce))
                else:
                    st.write('{} tablespoons {} is {} ounces'.format(self.amount, self.ingr, ounce))
            if need == 'milliliter':
                ml = round((self.amount*4.92892)*3, ndigits=2)
                if self.amount == 1:
                    st.write('{} tablespoon {} is {} milliliters'.format(self.amount, self.ingr, ml))
                elif ml <= 1:
                    st.write('{} tablespoons {} is {} milliliter'.format(self.amount, self.ingr, ml))
                else:
                    st.write('{} tablespoons {} is {} milliliters'.format(self.amount, self.ingr, ml))
            if need == 'teaspoon':
                tsp = round((self.amount*3), ndigits=2)
                if tsp <= 1:
                    st.write('{} tablespoons {} is {} teaspoon'.format(self.amount, self.ingr, tsp))
                elif self.amount == 1:
                    st.write('{} tablespoons {} is {} teaspoon'.format(self.amount, self.ingr, tsp))
                else:
                    st.write('{} tablespoons {} is {} teaspoons'.format(self.amount, self.ingr, tsp))
            if need == 'tablespoon':
                st.write('Whoops! You chose the same unit of measure that you already have. Try something else!')
            if need == 'pound':
                lb = round(((self.amount/16)*self.ouz)/16, ndigits=2)
                if self.amount == 1:
                    st.write('{} tablespoon {} is {} pouncds'.format(self.amount, self.ingr, lb))
                elif lb <= 1:
                    st.write('{} tablespoons {} is {} pound'.format(self.amount, self.ingr, lb))
                else:
                    st.write('{} tablespoons {} is {} pounds'.format(self.amount, self.ingr, lb))
            if need == 'liter':
                l = round((self.amount*0.0147868), ndigits=2)
                if self.amount == 1:
                    st.write('{} tablespoon {} is {} liters'.format(self.amount, self.ingr, l))
                elif l <= 1:
                    st.write('{} tablespoon {} is {} liters'.format(self.amount, self.ingr, l))
                else:
                    st.write('{} tablespoons {} is {} liters'.format(self.amount, self.ingr, l))
            if need == 'fluid ounce':
                floz = round((self.amount/2), ndigits=2)
                if self.amount == 1:
                    st.write('{} tablespoon {} is {} fluid ounces'.format(self.amount, self.ingr, floz))
                elif floz <= 1:
                    st.write('{} tablespoons {} is {} fluid ounce'.format(self.amount, self.ingr, floz))
                else:
                    st.write('{} tablespoons {} is {} fluid ounces'.format(self.amount, self.ingr, floz))
        elif self.measurement == 'pound':
            if need == 'gram':
                gram = round(self.amount*453.592, ndigits=2)
                if gram <= 1:
                    st.write('{} pounds {} is {} gram'.format(self.amount, self.ingr, gram))
                elif self.amount == 1:
                    st.write('{} pound {} is {} grams'.format(self.amount, self.ingr, gram))
                else:
                    st.write('{} pounds {} is {} grams'.format(self.amount, self.ingr, gram))
            if need == 'cup':
                cup = round((self.amount/self.ouz)*16, ndigits=2)
                if self.amount == 1:
                    st.write('{} pound {} is {} cups'.format(self.amount, self.ingr, cup))
                elif cup <= 1:
                    st.write('{} pounds {} is {} cup'.format(self.amount, self.ingr, cup))
                else:
                    st.write('{} pounds {} is {} cups'.format(self.amount, self.ingr, cup))
            if need == 'ounce':
                ounce = round(self.amount*16, ndigits=2)
                if self.amount == 1:
                    st.write('{} pound {} is {} ounces'.format(self.amount, self.ingr, ounce))
                elif ounce <= 1:
                    st.write('{} pounds {} is {} ounce'.format(self.amount, self.ingr, ounce))
                else:
                    st.write('{} pounds {} is {} ounce'.format(self.amount, self.ingr, ounce))
            if need == 'milliliter':
                ml = round(((self.amount/self.ouz)*236.588)*16, ndigits=2)
                if self.amount == 1:
                    st.write('{} pound {} is {} milliliters'.format(self.amount, self.ingr, ml))
                elif ml <= 1:
                    st.write('{} pounds {} is {} milliliter'.format(self.amount, self.ingr, ml))
                else:
                    st.write('{} pounds {} is {} milliliters'.format(self.amount, self.ingr, ml))
            if need == 'teaspoon':
                tsp = round(((self.amount*48)/self.ouz)*16, ndigits=2)
                if self.amount == 1:
                    st.write('{} pound {} is {} teaspoons'.format(self.amount, self.ingr, tsp))
                elif tsp <= 1:
                    st.write('{} pounds {} is {} teaspoon'.format(self.amount, self.ingr, tsp))
                else:
                    st.write('{} pounds {} is {} teaspoons'.format(self.amount, self.ingr, tsp))
            if need == 'tablespoon':
                tbsp = round(((self.amount*16)/self.ouz)*16, ndigits=2)
                if self.amount == 1:
                    st.write('{} pound {} is {} tablespoons'.format(self.amount, self.ingr, tbsp))
                elif tbsp <= 1:
                    st.write('{} pounds {} is {} tablespoon'.format(self.amount, self.ingr, tbsp))
                else:
                    st.write('{} pounds {} is {} tablespoons'.format(self.amount, self.ingr, tbsp))
            if need == 'pound':
                st.write('Whoops! You chose the same unit of measure that you already have. Try something else!')
            if need == 'liter':
                pass
            if need == 'fluid ounce':
                pass
        elif self.measurement == 'milliliter':
            if need == 'gram':
                gram = round((self.amount*self.grm)/236.588, ndigits=2)
                if self.amount == 1:
                    st.write('{}  milliliters {} is {} gram'.format(self.amount, self.ingr, gram))
                elif gram <= 1:
                    st.write('{}  milliliter {} is {} grams'.format(self.amount, self.ingr, gram))
                else:
                    st.write('{}  milliliters {} is {} grams'.format(self.amount, self.ingr, gram))
            if need == 'cup':
                cup = round(self.amount/236.588, ndigits=2)
                if self.amount == 1:
                    st.write('{}  milliliters {} is {} cup'.format(self.amount, self.ingr, cup))
                elif cup <= 1:
                    st.write('{}  milliliter {} is {} cups'.format(self.amount, self.ingr, cup))
                else:
                    st.write('{}  milliliters {} is {} cups'.format(self.amount, self.ingr, cup))
            if need == 'ounce':
                ounce = round((self.amount*self.ouz)/236.588, ndigits=2)
                if self.amount == 1:
                    st.write('{} milliliter {} is {} ounces'.format(self.amount, self.ingr, ounce))
                elif ounce <= 1:
                    st.write('{} milliliters {} is {} ounce'.format(self.amount, self.ingr, ounce))
                else:
                    st.write('{} milliliters {} is {} ounces'.format(self.amount, self.ingr, ounce))
            if need == 'milliliter':
                st.write('Whoops! You chose the same unit of measure that you already have. Try something else!')
            if need == 'teaspoon':
                tsp = round((self.amount/4.92892), ndigits=2)
                if tsp <= 1:
                    st.write('{} milliliters {} is {} teaspoon'.format(self.amount, self.ingr, tsp))
                elif self.amount == 1:
                    st.write('{} milliliters {} is {} teaspoons'.format(self.amount, self.ingr, tsp))
                else:
                    st.write('{} milliliters {} is {} teaspoons'.format(self.amount, self.ingr, tsp))
            if need == 'tablespoon':
                tbsp = round((self.amount/4.92892)/3, ndigits=2)
                if tbsp <= 1:
                    st.write('{} milliliters {} is {} tablespoon'.format(self.amount, self.ingr, tbsp))
                elif self.amount == 1:
                    st.write('{} milliliters {} is {} tablespoons'.format(self.amount, self.ingr, tbsp))
                else:
                    st.write('{} milliliters {} is {} tablespoons'.format(self.amount, self.ingr, tbsp))
            if need == 'pound':
                lb = round(((self.amount*self.ouz)/236.588)/16, ndigits=2)
                if self.amount == 1:
                    st.write('{} milliliter {} is {} pounds'.format(self.amount, self.ingr, lb))
                elif lb <= 1:
                    st.write('{} milliliters {} is {} pound'.format(self.amount, self.ingr, lb))
                else:
                    st.write('{} milliliters {} is {} pounds'.format(self.amount, self.ingr, lb))
            if need == 'liter':
                l = round(self.amount/1000, ndigits=2)
                if self.amount == 1:
                    st.write('{} milliliter {} is {} liters'.format(self.amount, self.ingr, l))
                elif l <= 1:
                    st.write('{} milliliters {} is {} liter'.format(self.amount, self.ingr, l))
                else:
                    st.write('{} milliliters {} is {} liters'.format(self.amount, self.ingr, l))
            if need == 'fluid ounce':
                floz = round(self.amount/29.5735, ndigits=2)
                if self.amount == 1:
                    st.write('{} milliliter {} is {} fluid ounces'.format(self.amount, self.ingr, floz))
                elif floz <= 1:
                    st.write('{} milliliters {} is {} fluid ounce'.format(self.amount, self.ingr, floz))
                else:
                    st.write('{} milliliters {} is {} fluid ounces'.format(self.amount, self.ingr, floz))
        elif self.measurement == 'liter':
            if need == 'gram':
                gram = round((self.amount*self.grm)/0.236588, ndigits=2)
                if self.amount == 1:
                    st.write('{} liter {} is {} grams'.format(self.amount, self.ingr, gram))
                elif gram <= 1:
                    st.write('{} liters {} is {} gram'.format(self.amount, self.ingr, gram))
                else:
                    st.write('{} liters {} is {} gram'.format(self.amount, self.ingr, gram))
            if need == 'cup':
                cup = round(self.amount*4.22675, ndigits=2)
                if self.amount == 1:
                    st.write('{} liter {} is {} cup'.format(self.amount, self.ingr, cup))
                elif cup <= 1:
                    st.write('{} liters {} is {} cups'.format(self.amount, self.ingr, cup))
                else:
                    st.write('{} liters {} is {} cups'.format(self.amount, self.ingr, cup))
            if need == 'ounce':
                pass
            if need == 'milliliter':
                ml = round(self.amount*1000, ndigits=2)
                if self.amount == 1:
                    st.write('{} liter {} is {} milliliter'.format(self.amount, self.ingr, ml))
                elif ml <= 1:
                    st.write('{} liters {} is {} milliliters'.format(self.amount, self.ingr, ml))
                else:
                    st.write('{} liters {} is {} milliliters'.format(self.amount, self.ingr, ml))
            if need == 'teaspoon':
                tsp = round((self.amount*67.628)*3, ndigits=2)
                if self.amount == 1:
                    st.write('{} liter {} is {} teaspoons'.format(self.amount, self.ingr, tsp))
                elif tsp <= 1:
                    st.write('{} liters {} is {} teaspoon'.format(self.amount, self.ingr, tsp))
                else:
                    st.write('{} liters {} is {} teaspoons'.format(self.amount, self.ingr, tsp))
            if need == 'tablespoon':
                tbsp = round(self.amount*67.628, ndigits=2)
                if self.amount == 1:
                    st.write('{} liter {} is {} tablespoons'.format(self.amount, self.ingr, tbsp))
                elif tbsp <= 1:
                    st.write('{} liters {} is {} tablespoon'.format(self.amount, self.ingr, tbsp))
                else:
                    st.write('{} liters {} is {} tablespoons'.format(self.amount, self.ingr, tbsp))
            if need == 'pound':
                pass
            if need == 'liter':
                st.write('Whoops! You chose the same unit of measure that you already have. Try something else!')
            if need == 'fluid ounce':
                floz = round(self.amount*33.814, ndigits=2)
                if self.amount == 1:
                    st.write('{} liter {} is {} fluid ounces'.format(self.amount, self.ingr, floz))
                elif floz <= 1:
                    st.write('{} liters {} is {} fluid ounce'.format(self.amount, self.ingr, floz))
                else:
                    st.write('{} liters {} is {} fluid ounces'.format(self.amount, self.ingr, floz))
        # elif self.measurement == 'fluid ounce':
        else:
            if need == 'gram':
                gram = round((self.amount*self.grm)/8, ndigits=2)
                if self.amount == 1:
                    st.write('{} fluid ounce {} is {} grams'.format(self.amount, self.ingr, gram))
                elif gram <= 1:
                    st.write('{} fluid ounces {} is {} gram'.format(self.amount, self.ingr, gram))
                else:
                    st.write('{} fluid ounces {} is {} grams'.format(self.amount, self.ingr, gram))
            if need == 'cup':
                cup = round(self.amount/8, ndigits=2)
                if self.amount == 1:
                    st.write('{} fluid ounce {} is {} cups'.format(self.amount, self.ingr, cup))
                elif cup <= 1:
                    st.write('{} fluid ounces {} is {} cup'.format(self.amount, self.ingr, cup))
                else:
                    st.write('{} fluid ounces {} is {} cups'.format(self.amount, self.ingr, cup))
            if need == 'ounce':
                ounce = round(((self.amount*self.grm)/8)/28.3495, ndigits=2)
                if self.amount == 1:
                    st.write('{} fluid ounce {} is {} ounces'.format(self.amount, self.ingr, ounce))
                elif ounce <= 1:
                    st.write('{} fluid ounces {} is {} ounce'.format(self.amount, self.ingr, ounce))
                else:
                    st.write('{} fluid ounces {} is {} ounces'.format(self.amount, self.ingr, ounce))
            if need == 'milliliter':
                ml = round(self.amount*29.5735, ndigits=2)
                if self.amount == 1:
                    st.write('{} fluid ounce {} is {} milliliters'.format(self.amount, self.ingr, ml))
                elif ml <= 1:
                    st.write('{} fluid ounces {} is {} milliliter'.format(self.amount, self.ingr, ml))
                else:
                    st.write('{} fluid ounces {} is {} milliliters'.format(self.amount, self.ingr, ml))
            if need == 'teaspoon':
                tsp = round((self.amount*6), ndigits=2)
                if self.amount == 1:
                    st.write('{} fluid ounce {} is {} teaspoons'.format(self.amount, self.ingr, tsp))
                elif tsp <= 1:
                    st.write('{} fluid ounces {} is {} teaspoon'.format(self.amount, self.ingr, tsp))
                else:
                    st.write('{} fluid ounces {} is {} teaspoons'.format(self.amount, self.ingr, tsp))
            if need == 'tablespoon':
                tbsp = round((self.amount*2), ndigits=2)
                if self.amount == 1:
                    st.write('{} fluid ounce {} is {} tablespoons'.format(self.amount, self.ingr, tbsp))
                elif tbsp <= 1:
                    st.write('{} fluid ounces {} is {} tablespoon'.format(self.amount, self.ingr, tbsp))
                else:
                    st.write('{} fluid ounces {} is {} tablespoons'.format(self.amount, self.ingr, tbsp))
            if need == 'pound':
                pass
            if need == 'liter':
                l = round(self.amount/33.814, ndigits=2)
                if self.amount == 1:
                    st.write('{} fluid ounce {} is {} liters'.format(self.amount, self.ingr, l))
                elif l <= 1:
                    st.write('{} fluid ounces {} is {} liter'.format(self.amount, self.ingr, l))
                else:
                    st.write('{} fluid ounces {} is {} liter'.format(self.amount, self.ingr, l))
            if need == 'fluid ounce':
                st.write('Whoops! You chose the same unit of measure that you already have. Try something else!')
        # elif self.measurement == 'fahrenheit':
        #     if need == 'celcius':
        #         c = round((self.amount-32)*(5/9), ndigits=2)
        #         if self.amount == 1:
        #             st.write('{} degree fahrenheit is {} degrees celcius'.format(self.amount, c))
        #         elif c <= 1:
        #             st.write('{} degrees fahrenheit is {} degree celcius'.format(self.amount, c))
        #         else:
        #             st.write('{} degrees fahrenheit is {} degrees celcius'.format(self.amount, c))
        #     else:
        #         st.write('Whoops! Sorry! This only work with celcius.')
        # else:
        #     if need == 'fahrenheit':
        #         f = round()
        #         if self.amount == 1:
        #             st.write('{} degree celcius is {} degrees fahrenheit'.format(self.amount, f))
        #         elif f <= 1:
        #             st.write('{} degrees celcius is {} degree fahrenheit'.format(self.amount, f))
        #         else:
        #             st.write('{} degrees celcius is {} degrees fahrenheit'.format(self.amount, f))
        #     else:
        #         st.write('Whoops! Sorry! This only work with fahrenheit.')

### Add gallon, pint, quart


# Define measurements for drop down list
# msmt = ['gram', 'cup', 'ounce', 'teaspoon', 'tablespoon', 'pound', 'milliliter', 
#         'liter', 'fluid ounce', 'fahrenheit', 'celcius']
msmt = ['gram', 'cup', 'ounce', 'teaspoon', 'tablespoon', 'pound', 'milliliter', 
        'liter', 'fluid ounce']

#Title the page
st.title('Conversions! :cake:')
st.subheader("Convert your ingredients easily! Just type in what you're using, how much you have, what the measurement is in, and what you need. Hit the yes button if it all looks good and you've got your new measurement!")

# First selection box to define your ingredient
# ingr = st.selectbox('What ingredient are you using?', df.index)
ingr = st.selectbox('What ingredient are you using?', sort(df.index))
ingr = ingr.lower()
# Second input to define how much you have
amount = st.number_input('How much do you have?')

####### Add something that shows the conversions of fractions to decimals!

# Define the measurement that you already have
measurement = st.radio('What measurement do you have?', msmt)

#Define the measurement that you need
need = st.radio('What measurement do you need?', msmt)

if amount <= 1:
    st.write('You need', amount, measurement, 'of', ingr, 'converted to', need + 's?')
else:
    st.write('You have', amount, measurement + 's', 'of', ingr, 'converted to', need + 's?')

if st.button('Yes!'):
    baking(ingr, amount, measurement, need)
#     def gram_to_cup(self, amount):
#         ''' Convert grams to cups
#         amount = how much of an item you have and wish to convert'''
#         cup = round(amount/self.grams_in_cup, ndigits=2)
#         if cup == 1:
#             return ('{} grams {} is {} cup').format(amount, self.item, cup)
#         else:
#             return ('{} grams {} is {} cups').format(amount, self.item, cup)
# grm = [df.loc[i, 'grams'] for i in df.index if i == ingr]
# grm = grm[0]
# ouz = [df.loc[i, 'ounces'] for i in df.index if i == ingr]
# ouz = ouz[0]                    
# st.sidebar.text('Tips!')

st.sidebar.markdown('**Quick References**')
# st.sidebar.text('\n')
st.sidebar.markdown('1 stick of butter is: 8 tablespoons, 113 grams, 4 ounces, 1/2 cup')
# st.sidebar.markdown('8 tablespoons, 113 grams, 4 ounces, 1/2 cup')
st.sidebar.text('3 teaspoons = 1 tablespoon')
st.sidebar.text('4 tablespoons = 1/4 cup')
st.sidebar.text('16 tablespoons = 1 cup')
st.sidebar.text('1 teaspoons = 5 mL')
st.sidebar.text('8 fluid ounces = 1 cup')
st.sidebar.text('1 ounce = 28 grams')
st.sidebar.text('16 ounces = 1 pound')
st.sidebar.image(fraction, width=150)
