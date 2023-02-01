from flask import render_template, request
from app import app
import sqlite3
import requests

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Choixquestionnaire',methods = ['GET','POST'])
def choix():
    if request.method=='POST':
        global ident
        global mot_de_passe
        authentication = request.form
        ident = authentication["ident"]
        mot_de_passe = authentication["mot_de_passe"]
        with sqlite3.connect("authentification.db") as con:
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS authentification(pseudo,mdp,score)")
            cur.execute("INSERT INTO authentification(pseudo,mdp) VALUES(?,?)", (ident, mot_de_passe))
            con.commit()
        con.close()
        return render_template('Choix questionnaire.html', ident=ident, mdp=mot_de_passe)
    else:
        return render_template('Choix questionnaire.html')

@app.route("/Questionnaire d'estime de soi",methods = ['POST'])
def estime_de_soi():
    return render_template("Questionnaire d'estime de soi.html")

@app.route("/Questionnaire d'affirmation de soi",methods = ['POST'])
def affirmation_de_soi():
    return render_template("Questionnaire d'affirmation de soi.html")

@app.route("/Questionnaire d’anxiété et de la dépression",methods = ['POST'])
def anxiete_et_depression():
    return render_template("Questionnaire d’anxiété et de la dépression.html")

@app.route("/Questionnaire d’anxiété sociale",methods = ['POST'])
def anxiete_sociale():
    return render_template("Questionnaire d’anxiété sociale.html")

@app.route("/Questionnaire de burn-out professionnel",methods = ['POST'])
def burn_out_professionnel():
    return render_template("Questionnaire de burn-out professionnel.html")

@app.route("/Resultats_questionnaire",methods = ['POST'])
def redirection():
    choix = request.form
    verification = choix["verification"]
    if verification == "estime":
        estime, nom_questionnaire = questionnaire_estime()
        return render_template("Resultats_questionnaire.html", conclusion=estime, nom_questionnaire=nom_questionnaire, ident=ident)
    elif verification == "affirmation":
        affirmation, nom_questionnaire = questionnaire_affirmation()
        return render_template("Resultats_questionnaire.html", conclusion=affirmation, nom_questionnaire=nom_questionnaire, ident=ident)
    elif verification == "anxiete et depression":
        anxiete, nom_questionnaire = questionnaire_anxiete_depression()
        return render_template("Resultats_questionnaire.html", conclusion=anxiete, nom_questionnaire=nom_questionnaire, ident=ident)
    elif verification == "burnout":
        burnout, nom_questionnaire = questionnaire_burnout()
        return render_template("Resultats_questionnaire.html", conclusion=burnout, nom_questionnaire=nom_questionnaire, ident=ident)
    elif verification == "anx_sociale":
        anx_sociale, nom_questionnaire = questionnaire_anxiete_sociale()
        return render_template("Resultats_questionnaire.html", conclusion=anx_sociale, nom_questionnaire=nom_questionnaire, ident=ident)

def questionnaire_estime():
    nom_questionnaire = "questionnaire d'estime de soi"
    estime = ""
    resultats = request.form
    resultat_1 = int(resultats["choice1"])
    resultat_2 = int(resultats["choice2"])
    resultat_3 = int(resultats["choice3"])
    resultat_4 = int(resultats["choice4"])
    resultat_5 = int(resultats["choice5"])
    resultat_6 = int(resultats["choice6"])
    resultat_7 = int(resultats["choice7"])
    resultat_8 = int(resultats["choice8"])
    resultat_9 = int(resultats["choice9"])
    resultat_10 = int(resultats["choice10"])
    somme = resultat_1 + resultat_2 + resultat_3 + resultat_4 + resultat_5 + resultat_6 + resultat_7 + resultat_8 + resultat_9 + resultat_10
    if somme<25:
        estime = "Votre estime de vous même est très faible. Un travail dans ce domaine semble souhaitable."
    elif 25<=somme<31:
        estime = "Votre estime de vous même est faible. Un travail dans ce domaine serait bénéfique."
    elif 31<=somme<34:
        estime = "Votre estime de vous même est dans la moyenne"
    elif 34<=somme<39:
        estime = "Votre estime de vous même est forte"
    else:
        estime = "Votre estime de vous même est très forte"
    return (estime,nom_questionnaire)

def questionnaire_affirmation():
    nom_questionnaire = "questionnaire d'affirmation de soi"
    affirmation = ""
    resultats = request.form
    resultat_1 = int(resultats["choice1"])
    resultat_2 = int(resultats["choice2"])
    resultat_3 = int(resultats["choice3"])
    resultat_4 = int(resultats["choice4"])
    resultat_5 = int(resultats["choice5"])
    resultat_6 = int(resultats["choice6"])
    resultat_7 = int(resultats["choice7"])
    resultat_8 = int(resultats["choice8"])
    resultat_9 = int(resultats["choice9"])
    resultat_10 = int(resultats["choice10"])
    resultat_11 = int(resultats["choice11"])
    resultat_12 = int(resultats["choice12"])
    resultat_13 = int(resultats["choice13"])
    resultat_14 = int(resultats["choice14"])
    resultat_15 = int(resultats["choice15"])
    resultat_16 = int(resultats["choice16"])
    resultat_17 = int(resultats["choice17"])
    resultat_18 = int(resultats["choice18"])
    resultat_19 = int(resultats["choice19"])
    resultat_20 = int(resultats["choice20"])
    resultat_21 = int(resultats["choice21"])
    resultat_22 = int(resultats["choice22"])
    resultat_23 = int(resultats["choice23"])
    resultat_24 = int(resultats["choice24"])
    resultat_25 = int(resultats["choice25"])
    resultat_26 = int(resultats["choice26"])
    resultat_27 = int(resultats["choice27"])
    resultat_28 = int(resultats["choice28"])
    resultat_29 = int(resultats["choice29"])
    resultat_30 = int(resultats["choice30"])
    somme = resultat_1 + resultat_2 + resultat_3 + resultat_4 + resultat_5 + resultat_6 + resultat_7 + resultat_8 + resultat_9 + resultat_10
    + resultat_11 + resultat_12 + resultat_13 + resultat_14 + resultat_15 + resultat_16 + resultat_17 + resultat_18 + resultat_19 + resultat_20
    + resultat_21 + resultat_22 + resultat_23 + resultat_24 + resultat_25 + resultat_26 + resultat_27 + resultat_28 + resultat_29 + resultat_30
    if somme<81:
        affirmation = "Vous avez un caractère hyperaffirmé voire agressif."
    elif 81<=somme<106:
        affirmation = "Vous êtes quelqu'un qui s'affirme dans la vie."
    elif 106<=somme<129:
        affirmation = "Vous êtes quelqu'un qui ne s'affirme pas beaucoup."
    else:
        affirmation = "Vous êtes quelqu'un de passif dans votre vie."
    return (affirmation, nom_questionnaire)


def questionnaire_anxiete_depression():
    nom_questionnaire = "questionnaire d'anxiété et de la dépression"
    anxiete = ""
    resultats = request.form
    resultat_1 = int(resultats["choice1"])
    resultat_2 = int(resultats["choice2"])
    resultat_3 = int(resultats["choice3"])
    resultat_4 = int(resultats["choice4"])
    resultat_5 = int(resultats["choice5"])
    resultat_6 = int(resultats["choice6"])
    resultat_7 = int(resultats["choice7"])
    resultat_8 = int(resultats["choice8"])
    resultat_9 = int(resultats["choice9"])
    resultat_10 = int(resultats["choice10"])
    resultat_11 = int(resultats["choice11"])
    resultat_12 = int(resultats["choice12"])
    resultat_13 = int(resultats["choice13"])
    resultat_14 = int(resultats["choice14"])
    somme_anxiete = resultat_1 + resultat_2 + resultat_3 + resultat_4 + resultat_5 + resultat_6 + resultat_7
    somme_depression = resultat_8 + resultat_9 + resultat_10+ resultat_11 + resultat_12 + resultat_13 + resultat_14
    somme = somme_depression + somme_anxiete
    if somme<=7:
        anxiete="Absence de symptomatologie"
    elif 4<=somme_anxiete<5:
        anxiete="Vous avez très probablement un état anxieux."
    elif 4<=somme_depression<5:
        anxiete="Vous avez très probablement un état dépressif."
    elif 4<=somme_depression<5 & 4<=somme_anxiete<5:
        anxiete="Vous avez très probablement un état anxieux et dépressif."
    elif 5<=somme_anxiete:
        anxiete="Vous avez un état anxieux certain."
    elif 5<=somme_depression:
        anxiete="Vous avez un état dépressif certain."
    elif 5<=somme_anxiete & 5<=somme_depression:
        anxiete="Vous avez un état anxieux et dépressif certain."
    return (anxiete,nom_questionnaire)

def questionnaire_burnout():
    nom_questionnaire = "Questionnaire de burn-out professionnel"
    burnout = ""
    resultats = request.form
    resultat_1 = int(resultats["choice1"])
    resultat_2 = int(resultats["choice2"])
    resultat_3 = int(resultats["choice3"])
    resultat_4 = int(resultats["choice4"])
    resultat_5 = int(resultats["choice5"])
    resultat_6 = int(resultats["choice6"])
    resultat_7 = int(resultats["choice7"])
    resultat_8 = int(resultats["choice8"])
    resultat_9 = int(resultats["choice9"])
    resultat_10 = int(resultats["choice10"])
    resultat_11 = int(resultats["choice11"])
    resultat_12 = int(resultats["choice12"])
    resultat_13 = int(resultats["choice13"])
    resultat_14 = int(resultats["choice14"])
    resultat_15 = int(resultats["choice15"])
    resultat_16 = int(resultats["choice16"])
    resultat_17 = int(resultats["choice17"])
    resultat_18 = int(resultats["choice18"])
    resultat_19 = int(resultats["choice19"])
    resultat_20 = int(resultats["choice20"])
    resultat_21 = int(resultats["choice21"])
    resultat_22 = int(resultats["choice22"])
    somme_SEP = resultat_1 + resultat_2 + resultat_3 + resultat_6 + resultat_8 + resultat_13 + resultat_14 + resultat_16 + resultat_20
    somme_SD = resultat_5 + resultat_10 + resultat_11 + resultat_15 + resultat_22
    somme_SAP = resultat_4 + resultat_7 + resultat_9 + resultat_12 + resultat_17 + resultat_18 + resultat_19 + resultat_21
    if somme_SEP <17:
        burnout = "Vous avez un degré faible d'épuisement professionnel"
    elif 18<somme_SEP<29:
        burnout = "Vous avez un degré modéré d'épuisement professionnel"
    else:
        burnout = "Vous avez un degré élevé d'épuisement professionnel"
    if somme_SD<5:
        burnout = burnout + " et un degré faible de dépersonnalition."
    elif 6<somme_SD<11:
        burnout = burnout + " et un degré modéré de dépersonnalition."
    else:
        burnout = burnout + " et un degré élevé de dépersonnalition."
    if somme_SAP<33:
        burnout = burnout + "De plus, vous avez un degré faible d'accomplissement personnel."
    elif 34<somme_SAP<39:
        burnout = burnout + "De plus, vous avez un degré modéré d'accomplissement personnel."
    else:
        burnout = burnout + "De plus, vous avez un degré élevé d'accomplissement personnel."
    return (burnout, nom_questionnaire)

def questionnaire_anxiete_sociale():
    nom_questionnaire = "questionnaire d'anxiété sociale"
    anx_sociale = ""
    resultats = request.form
    resultat_1a = int(resultats["choice11"])
    resultat_2a = int(resultats["choice21"])
    resultat_3a = int(resultats["choice31"])
    resultat_4a = int(resultats["choice41"])
    resultat_5a = int(resultats["choice51"])
    resultat_6a = int(resultats["choice61"])
    resultat_7a = int(resultats["choice71"])
    resultat_8a = int(resultats["choice81"])
    resultat_9a = int(resultats["choice91"])
    resultat_10a = int(resultats["choice101"])
    resultat_11a = int(resultats["choice111"])
    resultat_12a = int(resultats["choice121"])
    resultat_13a = int(resultats["choice131"])
    resultat_14a = int(resultats["choice141"])
    resultat_15a = int(resultats["choice151"])
    resultat_16a = int(resultats["choice161"])
    resultat_17a = int(resultats["choice171"])
    resultat_18a = int(resultats["choice181"])
    resultat_19a = int(resultats["choice191"])
    resultat_20a = int(resultats["choice201"])
    resultat_21a = int(resultats["choice211"])
    resultat_22a = int(resultats["choice221"])
    resultat_23a = int(resultats["choice231"])
    resultat_24a = int(resultats["choice241"])
    resultat_1b = int(resultats["choice12"])
    resultat_2b = int(resultats["choice22"])
    resultat_3b = int(resultats["choice32"])
    resultat_4b = int(resultats["choice42"])
    resultat_5b = int(resultats["choice52"])
    resultat_6b = int(resultats["choice62"])
    resultat_7b = int(resultats["choice72"])
    resultat_8b = int(resultats["choice82"])
    resultat_9b = int(resultats["choice92"])
    resultat_10b = int(resultats["choice102"])
    resultat_11b = int(resultats["choice112"])
    resultat_12b = int(resultats["choice122"])
    resultat_13b = int(resultats["choice132"])
    resultat_14b = int(resultats["choice142"])
    resultat_15b = int(resultats["choice152"])
    resultat_16b = int(resultats["choice162"])
    resultat_17b = int(resultats["choice172"])
    resultat_18b = int(resultats["choice182"])
    resultat_19b = int(resultats["choice192"])
    resultat_20b = int(resultats["choice202"])
    resultat_21b = int(resultats["choice212"])
    resultat_22b = int(resultats["choice222"])
    resultat_23b = int(resultats["choice232"])
    resultat_24b = int(resultats["choice242"])
    somme = resultat_1a + resultat_2a + resultat_3a + resultat_4a + resultat_5a + resultat_6a + resultat_7a + resultat_8a + resultat_9a + resultat_10a + resultat_11a
    + resultat_12a + resultat_13a + resultat_14a + resultat_15a + resultat_16a + resultat_17a + resultat_18a + resultat_19a + resultat_20a + resultat_21a + resultat_22a
    + resultat_23a + resultat_24a + resultat_1b + resultat_2b + resultat_3b + resultat_4b + resultat_5b + resultat_6b + resultat_7b + resultat_8b + resultat_9b + resultat_10b
    + resultat_11b + resultat_12b + resultat_13b + resultat_14b + resultat_15b + resultat_16b + resultat_17b + resultat_18b + resultat_19b + resultat_20b + resultat_21b
    + resultat_22b + resultat_23b + resultat_24b
    if somme>0:
        anx_sociale = "Vous n'avez pas de phobie sociale"
    elif 56<anx_sociale<=65:
        anx_sociale = "Vous avez une phobie sociale modérée"
    elif 66<=anx_sociale<=80:
        anx_sociale = "Vous avez une phobie sociale marquée"
    elif 81<=anx_sociale<=95:
        anx_sociale = "Vous avez une phobie sociale sévère"
    else:
        anx_sociale = "Vous avez une phobie sociale très sévère"
    return (anx_sociale, nom_questionnaire)