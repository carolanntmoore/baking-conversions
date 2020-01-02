import pandas as pd
import streamlit as st

#Define measurements for drop down list
msmt = ['gram', 'cup', 'milliliter', 'ounce', 'teaspoon', 'tablespoon', 'pound', 'milliliter', 
        'liter', 'fluid ounce']

#Title the page
st.title('Conversions!')

# First selection box to define your ingredient
ingr = st.selectbox('What ingredient are you using?', df.index)

# Second input to define how much you have
amount = st.number_input('How much do you have?')

####### Add something that shows the conversions of fractions to decimals!

# Define the measurement that you already have
measurement = st.radio('What measurement do you have?', msmt)

#Define the measurement that you need
need = st.radio('What measurement do you need?', msmt)

details = [ingr, amount, measurement, need]

grm = [df.loc[i, 'grams'] for i in df.index if i == ingr]
grm = grm[0]
ouz = [df.loc[i, 'ounces'] for i in df.index if i == ingr]
ouz = ouz[0]
# fl = baking(grams, ounces, item)
# fl.gram_to_ounce(452)

fl = baking(grm, ouz, ingr)
function = ('fl.%s_to_%s(%d)' % (measurement, need, amount))


### Change this so that it'll show the ingr in order of multi select
### Maybe add ingr selections to a list and then use indexing to put them in?
### Do the same thing for the measurements
# if amount <= 1:
#     st.write('You have', amount, measurement, 'of', ingr, 'and need', need + 's,', 'correct?')
# else:
#     st.write('You have', amount, measurement + 's', 'of', ingr, 'and need', need + 's,', 'correct?')

if amount <= 1:
    st.write('You need', amount, measurement, 'of', ingr, 'converted to', need + 's?')
else:
    st.write('You have', amount, measurement + 's', 'of', ingr, 'converted to', need + 's?')

if st.button('Yes!'):
    st.write(function)