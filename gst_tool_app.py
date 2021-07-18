#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 00:14:05 2021

@author: shyambhu.mukherjee
"""
full_amount = 0
import streamlit as st
st.title("Rubberfy gst calculator")
st.subheader("Order type")
text = st.radio("order type",('COD','ONLINE'))
if text == 'COD':
    cod_money = 40
else:
    cod_money = 0

text = st.text_input("Enter item MRPs here")
print(text)
item_list = text.split(",")

if st.button("All item added"):
    print(item_list)
    item_list = [int(val) for val in item_list]
    sum_cost = sum(item_list)
    if sum_cost<500:
        ship_money = 30
    else:
        ship_money = 0
    full_amount = sum_cost+ship_money + cod_money
    pre_gst_cost = round(full_amount * 100/118,0)
    gst_cost = round(18*pre_gst_cost/100,2)
    round_off = round(full_amount - (pre_gst_cost+gst_cost),2)
    without_sep_charge = pre_gst_cost - (cod_money+ship_money)
    pre_gst_items = []
    for i in range(len(item_list)-1):
        pre_gst_items.append(round(item_list[i]/sum_cost*without_sep_charge,0))
    total_val_upto_last = sum(pre_gst_items)
    last_value = without_sep_charge-total_val_upto_last
    pre_gst_items.append(last_value)
    
    for i in range(len(item_list)):
        st.write("initial cost of item:",item_list[i],"final cost of item:",\
                 pre_gst_items[i])
    st.write("cod money",cod_money)
    st.write("shipping charges",ship_money)
    st.write("pre gst cost",pre_gst_cost)
    st.write("gst cost",gst_cost)
    st.write("round-off",round_off)
    st.write("full money",full_amount)
else:
    st.write("waiting for order")