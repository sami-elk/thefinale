import streamlit as st
import pandas as pd 
import csv
import matplotlib
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt 
import matplotlib
import seaborn as sns #Data Visualization library based on matplotlib
import base64
import codecs
import streamlit.components.v1 as stc 
import preprojet
def main():
    global file
    menu=["Accueil","Information","Filtrage","Diagramme"]
    choix=st.sidebar.selectbox("Menu",menu)
    operation=[]
    t1 = r"t1.PNG"
    t2 = r"python.png"
    t3 = r"t3.jpeg"
    logo = r"icons.png"
    if choix=="Accueil" :
        #st.title("Bienvenue sur notre site ")
        
        
        st.markdown(f"""<p>
                    <img style="float:left; height: 50px;
            width: 50px;"  src="data:image/png;base64,{base64.b64encode(open(logo, "rb").read()).decode()}"></p>
                    <h2 style="font-family:Bradley Hand, cursive;"> SanSamSak</h2>""", unsafe_allow_html=True)
        st.markdown(f"""<p >
                    <img style="float:right; height: 250px;
            width: 350px;" class="logo-img" src="data:image/png;base64,{base64.b64encode(open(t1, "rb").read()).decode()}">
                    </p><br><br>
                    <h2 class="sc-1vqnue2-2 DnHbM">Nous simplifions la gestion des fichiers <span style="color : #61C653;">CSV</span></h2>""", unsafe_allow_html=True)

        st.markdown("""<center><hr size="6" width="50%"  color="#838982"></center>""", unsafe_allow_html=True)
        st.markdown(f"""<p >
                            <img style="float:left; height: 250px;
            width: 350px;" class="logo-img" src="data:image/png;base64,{base64.b64encode(open(t2, "rb").read()).decode()}">
                            </p><br>
                            <h2 style="font-family:Verdana, sans-serif; padding-left:55%;">Filtrage des données </h2>
                            <p style="font-family:Andale Mono, monospace;-webkit-font-smoothing: antialiased;
            font-stretch: 400;
            font-weight: 400;padding-left:55%;">Supprimer des colonnes, supprimer les redondances.
                                        Renommer des colonnes.
                                    </p>""", unsafe_allow_html=True)

        st.markdown("""<center><hr size="6" width="50%"  color="#838982"></center>""", unsafe_allow_html=True)
        st.markdown(f"""<p >
                            <img style="float:right;height: 250px;
            width: 350px;" class="logo-img" src="data:image/png;base64,{base64.b64encode(open(t3, "rb").read()).decode()}">
                            </p><br>
                            <h2 style="font-family:Verdana, sans-serif;">Gestion des graphes</h2>
                                    <p style="font-family:Andale Mono, monospace;">Construire des graphes (Courbes, Diagramme circulaire ...).</p>
                                    """, unsafe_allow_html=True)
                            
    if choix=="Information" :
        st.markdown(f"""<p>
                    <img style="float:left; height: 50px;
            width: 50px;"  src="data:image/png;base64,{base64.b64encode(open(logo, "rb").read()).decode()}"></p>
                    <h2 style="font-family:Bradley Hand, cursive;"> SanSamSak</h2>""", unsafe_allow_html=True)
        
        st.markdown(f"""<h2 style="font-family:Bradley Hand, cursive;font-size:50px"> Information sur les données</h2>""", unsafe_allow_html=True)
        data = st.file_uploader("Importer un fichier", type=["csv"])  
        if data is not None : 
            df = importFile(data)
            file=df
        st.subheader("Affichage de fichier")
        if st.button("Visualiser les données"):
            st.dataframe(afficheFile(file))
        
        st.subheader("Type de données")
        if st.button("Visualiser les types des données"):
            st.write(datatype(file))
    if choix=="Filtrage" :
        st.markdown(f"""<p>
                    <img style="float:left; height: 50px;
            width: 50px;"  src="data:image/png;base64,{base64.b64encode(open(logo, "rb").read()).decode()}"></p>
                    <h2 style="font-family:Bradley Hand, cursive;"> SanSamSak</h2>""", unsafe_allow_html=True)
        
        st.markdown(f"""<h2 style="font-family:Bradley Hand, cursive;font-size:50px"> Filtrage des données</h2>""", unsafe_allow_html=True)
        st.subheader("Filtrage")
        data = st.file_uploader("Importer un fichier", type=["csv"])  
       # test = st.uploaded_file.fullpath
        #st.write(test)
        if data is not None : 
            df = importFile(data)
            file=df
            #Fichier_final(df)
        choix=listColo=["Supprimer des colonnes","Rennomer des colonnes","Supression les rebondances","Detecter les valeurs aberrantes"]
        for i in listColo :
            operation.append(st.checkbox(i))
        
        #suppression
        if operation[0]  :
            st.write("Selectinner des colonnes")
            all_columns_names = file.columns.tolist()
            selected_columns_names = st.multiselect("Select Columns To Plot",all_columns_names)
            if operation[0] :
                for j in selected_columns_names :					
                    file=file.drop(j, axis=1)
                    
        #rennomage
        
        text={}
        if operation[1]  :
            #df=importFile(aa)
            st.write("Selectinner des colonnes")
            listColo=[i for i in file.columns]
            for i in listColo :
                text[i]=st.text_input("Rennomer la colonne "+i )
            if operation[1] :
                for i in text :
                    if text[i] :
                        file.rename(columns={i : text[i]},inplace = True)	
                        
        #supression des rebondences
        if operation[2]  :
            file.drop_duplicates(keep = 'first', inplace=True)
            st.success("Les rebondences sont supprimées correctement")
        # Customizable Plot
        if operation[3] :
            all_columns_names = file.columns.tolist()
            type_of_plot = "box"
            selected_columns_names = st.multiselect("Select Columns To Plot",all_columns_names)

            if st.button("Visualiser les valeurs aberrantes"):

                # Custom Plot
                if type_of_plot:
                    cust_plot= df[selected_columns_names].plot(kind=type_of_plot)
                    st.write(cust_plot)
                    st.set_option('deprecation.showPyplotGlobalUse', False)
                    st.pyplot()
            if st.button("Supprimer les valeurs aberrantes"):
                Q1 = file.quantile(0.25)
                Q3 = file.quantile(0.75)
                IQR = Q3 - Q1
                file = file[~((file < (Q1 - 1.5 * IQR)) | (file > (Q3 + 1.5 * IQR))).any(axis=1)]
                st.success("Les valeurs aberrantes sont supprimées correctement")
                  
        if data :
            st.write("Cliquez pour telechrager votre document apres filtrage")
            if st.button("telecharger ") :
                Fichier_final(file)
                st.success("Votre fichier est telechrge sous nom 'Fichier.csv'")
    if choix=="Diagramme" :
        st.markdown(f"""<p>
                    <img style="float:left; height: 50px;
            width: 50px;"  src="data:image/png;base64,{base64.b64encode(open(logo, "rb").read()).decode()}"></p>
                    <h2 style="font-family:Bradley Hand, cursive;"> SanSamSak</h2>""", unsafe_allow_html=True)
        
        #Fonctionnalités générales 
        st.markdown(f"""<h2 style="font-family:Bradley Hand, cursive;font-size:50px"> Visualisation des graphes</h2>""", unsafe_allow_html=True)
        options = ["EDA","Plots"]   
        choice = st.sidebar.selectbox("Selectionner l'Option désirer",options)
        #Options disponnible dans la rubrique EDA
        if choice == 'EDA':
            st.subheader("Visualisation Statistique des données (EDA)")
 
            data = st.file_uploader("Importer un fichier", type=["csv"])   #Importation+type de fichier
            #Lecture du fichier importer 
            if data is not None: 
                df = pd.read_csv(data)
                
            #Affiche la dimension du tableau 
                if st.checkbox("Afficher la Dimension"):
                    st.write(df.shape)
            
            #Affiche le noms des colonnes 
                if st.checkbox("Afficher le nom des Colonnes"):
                    all_columns = df.columns.to_list()
                    st.write(all_columns)
            #Affiche les colonnes trier selon le choix de l'utilisateur
                if st.checkbox("Afficher les Colonnes souhaitées"):
                    selected_columns = st.multiselect("Choisir les Colonnes",all_columns)
                    new_df = df[selected_columns]
                    st.dataframe(new_df)

            #Affiche un résumé statistique du fichier 
                if st.checkbox("Summary"):
                    st.write(df.describe())
 
            #Affichages des HEAT MAPS : Matplotlib & Seaborn  
                if st.checkbox("Carte Thermique: Heat Maps (Matplotlib)"):
                    plt.matshow(df.corr())
                    st.pyplot()
            
                if st.checkbox("Carte Thermique : Heat Maps (Seaborn)"):
                    st.write(sns.heatmap(df.corr(),annot=True))
                    st.pyplot()
 
            #Affichage du diagramme circulaire (Pie Chart)
                if st.checkbox("Diagramme Circulaire (Pie Chart)"):
                    all_columns = df.columns.to_list()
                    column_to_plot = st.selectbox("Choisir 1 colonne ",all_columns)
                    pie_plot = df[column_to_plot].value_counts().plot.pie(autopct="%1.1f%%")
                    st.write(pie_plot)
                    st.pyplot()
 
        elif choice == 'Plots':
            st.subheader("Visualisation des Plots ( Graphes)")
            data = st.file_uploader("Importer un fichier", type=["csv", "txt", "xlsx"])
            #Lecture du fichier importer
            if data is not None:
                df = pd.read_csv(data)
                st.dataframe(df.head())
 
 
                if st.checkbox("Show Value Counts"):
                    st.write(df.iloc[:,-1].value_counts().plot(kind='bar'))
                    st.pyplot()
            
                # Customizable Plot
 
                all_columns_names = df.columns.tolist()
                type_of_plot = st.selectbox("Choisir un type de graphe",["Surfacique","À barre","Line", "hist"])
                selected_columns_names = st.multiselect("Selectionner les colonnes à afficher",all_columns_names)
 
                if st.button("Visualisation"):
                    #Affichage des plots selon les colonnes selectionner
                    st.success("Generating Customizable Plot of {} for {}".format(type_of_plot,selected_columns_names))
 
                    # Plot By Streamlit
                    if type_of_plot == 'Surfacique':
                        cust_data = df[selected_columns_names]
                        st.area_chart(cust_data)
 
                    elif type_of_plot == 'À barre':
                        cust_data = df[selected_columns_names]
                        st.bar_chart(cust_data)
 
                    elif type_of_plot == 'Line':
                        cust_data = df[selected_columns_names]
                        st.line_chart(cust_data)
 
                    
                    elif type_of_plot:
                        cust_plot= df[selected_columns_names].plot(kind=type_of_plot)
                        st.write(cust_plot)
                        st.pyplot()

if __name__=='__main__' :
    main()

        

        
            
