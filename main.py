import streamlit as st
import pickle
import numpy as np

pipe = pickle.load(open("pipe.pkl","rb"))
df = pickle.load(open("df.pkl","rb"))


st.title("laptop price")


company = st.selectbox("brand",df["Company"].unique())
type = st.selectbox("type",df["TypeName"].unique())
ram = st.selectbox("ram",df["Ram"].unique())
weight = st.number_input("weight of the laptop")
touchscreen = st.selectbox("touchscreen",["no","yes"])
ips = st.selectbox("ips",["no","yes"])
#ppi
s_size = st.number_input("screen_size")
resolution = st.selectbox("screen_resolution",["1366x768","1920x1080","1600x900","1440x900","1280x800","2880X1800","1280x720","3200X1800","2560x1440","2560x1600","2304x1440","3840x2160"
])

#cpu
cpu = st.selectbox("cpu",df["processor_name"].unique())
#hdd
hdd=  st.selectbox("HDD(in GB)",[0,128,256,512,1024,2048])
ssd = st.selectbox("SDD(in GB)",[0,8,128,256,512,1024])
gpu = st.selectbox("gpu",df["Gpu brand"].unique())
os = st.selectbox("os",df["os"].unique())
if st.button("predict price"):
    #querypoint
    ppi = None
    if touchscreen=="Yes":
        touchscreen = 1
    else:
        touchscreen = 0
    if ips == "Yes":
        ips =1
    else:
        ips = 0
    x_res = int(resolution.split("x")[0])
    y_res = int(resolution.split("x")[1])
    ppi = ((x_res**2)+(y_res**2))**0.5/s_size
    query = np.array([company,type,ram,weight,cpu,touchscreen,ips,ppi,hdd,ssd,gpu,os])
    query = query.reshape(1,12)
    st.title(int(np.exp(pipe.predict(query))))
