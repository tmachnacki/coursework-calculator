import time
import os
import sqlite3
import requests
import pdb
 
from bs4 import BeautifulSoup

#THERE IS DUPLICATE CODE BECAUSE WE REALIZED WE WERE MISSING ENG CLASSES
# They needed to be scraped slightly differently

def getlinks():
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    url = "https://www.lsa.umich.edu/cg/cg_openclasses.aspx"

    resp = requests.get(url, headers={'user-agent': user_agent}, timeout=15.0)
    soup = BeautifulSoup(resp.content, features="html.parser")
    table = soup.find(id="contentMain_DisplayResults_datalst")
    links = table.findAll('a')
    list_of_links = []
    for link in links:
        whole_link = "https://www.lsa.umich.edu/cg/" + link.get("href")
        list_of_links.append(whole_link)

    return list_of_links


def getCredit_Workload_Title(url):

    cookies_dict = {"sessionid": os.environ.get("COOKIE")}
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    # url = "https://atlas.ai.umich.edu/course/AAS%20125/"
    try:
        resp = requests.get(url, headers={'user-agent': user_agent}, timeout=15.0, cookies=cookies_dict)
    except:
        return None, None
    soup = BeautifulSoup(resp.content, features="html.parser")
    span = soup.find("span", {"class": "course-credit-label"})
    if span is not None:
        credit = span.text
        credit = credit.split()
        try:
            credit_hours = int(float(credit[0]))
        except:
            credit_hours = None
    else:
        credit_hours = None
    title_text = None
    title = soup.find("h1", {"class": "text-large"})
    if title is not None:
        title_text = title.text

    workload = soup.find("evaluation-card", {"class-prefix": "workload"})
    
    
    if workload is None or workload.get(":value") == "null":
        workload = None
    else:
        workload = int(float(workload.get(":value")))


    return credit_hours, workload, title_text


def getCredit_Workload(url):

    cookies_dict = {"sessionid": os.environ.get("COOKIE")}
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    # url = "https://atlas.ai.umich.edu/course/AAS%20125/"
    try:
        resp = requests.get(url, headers={'user-agent': user_agent}, timeout=15.0, cookies=cookies_dict)
    except:
        return None, None
    soup = BeautifulSoup(resp.content, features="html.parser")
    span = soup.find("span", {"class": "course-credit-label"})
    if span is not None:
        credit = span.text
        credit = credit.split()
        try:
            credit_hours = int(float(credit[0]))
        except:
            credit_hours = None
    else:
        credit_hours = None
    workload = soup.find("evaluation-card", {"class-prefix": "workload"})
    
    
    if workload is None or workload.get(":value") == "null":
        workload = None
    else:
        workload = int(float(workload.get(":value")))


    return credit_hours, workload


def addEngClasses():
    conn = sqlite3.connect('sql/db.sqlite3')
    cur = conn.cursor()
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    links = ["https://www.lsa.umich.edu/cg/cg_results.aspx?termArray=f_21_2360&cgtype=ug&department=EECS&show=10000",
            "https://www.lsa.umich.edu/cg/cg_results.aspx?termArray=f_21_2360&cgtype=ug&department=NERS&show=10000",
            "https://www.lsa.umich.edu/cg/cg_results.aspx?termArray=f_21_2360&cgtype=ug&department=AEROSP&show=10000",
            "https://www.lsa.umich.edu/cg/cg_results.aspx?termArray=f_21_2360&cgtype=ug&department=BIOMEDE&show=10000",
            "https://www.lsa.umich.edu/cg/cg_results.aspx?termArray=f_21_2360&cgtype=ug&department=CHE&show=10000",
            "https://www.lsa.umich.edu/cg/cg_results.aspx?termArray=f_21_2360&cgtype=ug&department=CLIMATE&show=10000",
            "https://www.lsa.umich.edu/cg/cg_results.aspx?termArray=f_21_2360&cgtype=ug&department=SPACE&show=10000",
            "https://www.lsa.umich.edu/cg/cg_results.aspx?termArray=f_21_2360&cgtype=ug&department=ENGR&show=10000",
            "https://www.lsa.umich.edu/cg/cg_results.aspx?termArray=f_21_2360&cgtype=ug&department=ENTR&show=10000",
            "https://www.lsa.umich.edu/cg/cg_results.aspx?termArray=f_21_2360&cgtype=ug&department=IOE&show=10000",
            "https://www.lsa.umich.edu/cg/cg_results.aspx?termArray=f_21_2360&cgtype=ug&department=AUTO&show=10000",
            "https://www.lsa.umich.edu/cg/cg_results.aspx?termArray=f_21_2360&cgtype=ug&department=MACROMOL&show=10000",
            "https://www.lsa.umich.edu/cg/cg_results.aspx?termArray=f_21_2360&cgtype=ug&department=MATSCIE&show=10000",
            "https://www.lsa.umich.edu/cg/cg_results.aspx?termArray=f_21_2360&cgtype=ug&department=MECHENG&show=10000",
            "https://www.lsa.umich.edu/cg/cg_results.aspx?termArray=f_21_2360&cgtype=ug&department=AERO&show=10000",
            "https://www.lsa.umich.edu/cg/cg_results.aspx?termArray=f_21_2360&cgtype=ug&show=20&department=NAVARCH",
            "https://www.lsa.umich.edu/cg/cg_results.aspx?termArray=f_21_2360&cgtype=ug&department=ROB&show=10000",
            "https://www.lsa.umich.edu/cg/cg_results.aspx?termArray=f_21_2360&cgtype=ug&department=TCHNCLCM&show=10000",
            ]
    prefix = "https://www.lsa.umich.edu/cg/"
    class_webpages = set()
    class_atlas_links = set()
    for link in links:
        try:
            resp = requests.get(link, headers={'user-agent': user_agent}, timeout=7.0)
        except:
            print(link)
            continue
        soup = BeautifulSoup(resp.content, features="html.parser")
        class_rows = soup.findAll("div", {"class":"ClassRow"})
        for class_row in class_rows:
            class_webpages.add(prefix+class_row.get("data-url"))

    for webpage in class_webpages:
        try:
            resp = requests.get(webpage, headers={'user-agent': user_agent}, timeout=7.0)
        except:
            print(link)
            continue
        soup = BeautifulSoup(resp.content, features="html.parser")
        atlas_button = soup.find(id="contentMain_lnk_ART2")
        class_atlas_links.add(atlas_button.get("href"))
        
    for atlas_link in class_atlas_links:

        portions = atlas_link.rsplit("/", 1)
        portions = portions[1].split("%20")
        department = portions[0]
        classnumber = portions[1]
        classname = department + " " + classnumber
        classnumber = int(classnumber)
        try:
            credit, workload, class_title = getCredit_Workload_Title(atlas_link)
        except:
            print("not enough values to unpack for some reason")
            continue
        sql = ''' INSERT INTO classes(classname,department,classnumber,title,credits,workload)
                                VALUES(?,?,?,?,?,?) '''
        tupl = (classname, department, classnumber, class_title, credit, workload)            
        if workload == None and credit == None:
            print("workload/credit is None")
            sql = ''' INSERT INTO classes(classname,department,classnumber,title)
                    VALUES(?,?,?,?) '''
            tupl = (classname, department, classnumber, class_title)
        elif workload == None:
            print("workload is None")
            sql = ''' INSERT INTO classes(classname,department,classnumber,title,credits)
                    VALUES(?,?,?,?,?) '''
            tupl = (classname, department, classnumber, class_title, credit)
        elif credit == None:
            print("workload/credit is None")
            sql = ''' INSERT INTO classes(classname,department,classnumber,title,workload)
                    VALUES(?,?,?,?,?) '''
            tupl = (classname, department, classnumber, class_title, workload)
        print(tupl)
        try:
            cur.execute(sql, tupl)
            conn.commit()
        except:
            print("unique error")

            
def main():

    #This does all the Eng classes
    addEngClasses()
    # return

    #This does all the LSA classes
    links = getlinks()

    conn = sqlite3.connect('sql/db.sqlite3')
    cur = conn.cursor()

    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"

    for link in links:
        # if link != "https://www.lsa.umich.edu/cg/cg_openclasses.aspx?txtsubject=ITALIAN":
        #     continue
        subject = link.split('=', 1)
        try:
            resp = requests.get(link, headers={'user-agent': user_agent}, timeout=15.0)
        except:
            continue
        soup = BeautifulSoup(resp.content, features="html.parser")
        table = soup.find(id="contentMain_Open_Classes_grdvw")
        table_rows = table.findAll('tr')
        count = -1
        ids_seen = []
        for table_row in table_rows:
            count += 1
            if count == 0 or count == 1:
                continue
            cols = table_row.findAll('td')
            num = 0
            for col in cols:
                #retrieve class id
                if num % 4 == 1 :
                    #skip this row we already have this class id
                    if int(col.text) in ids_seen:
                        break
                    class_id = int(col.text)
                    ids_seen.append(class_id)
                #retrieve title
                elif num % 4 == 2:
                    class_title = col.text
                elif num % 4 == 3:
                    
                    sql = ''' INSERT INTO classes(classname,department,classnumber,title,credits,workload)
                                VALUES(?,?,?,?,?,?) '''
                    classname = subject[1] + " " + str(class_id)
                    extra = subject[1] + "%20"+ str(class_id) + "/"
                    credit, workload = getCredit_Workload("https://atlas.ai.umich.edu/course/"+extra)
                    tupl = (classname, subject[1], class_id, class_title, credit, workload)
                    if workload == None and credit == None:
                        print("workload/credit is None")
                        sql = ''' INSERT INTO classes(classname,department,classnumber,title)
                                VALUES(?,?,?,?) '''
                        tupl = (classname, subject[1], class_id, class_title)
                    elif workload == None:
                        print("workload is None")
                        sql = ''' INSERT INTO classes(classname,department,classnumber,title,credits)
                                VALUES(?,?,?,?,?) '''
                        tupl = (classname, subject[1], class_id, class_title, credit)
                    elif credit == None:
                        print("workload/credit is None")
                        sql = ''' INSERT INTO classes(classname,department,classnumber,title,workload)
                                VALUES(?,?,?,?,?) '''
                        tupl = (classname, subject[1], class_id, class_title, workload)


                    print(tupl)
                    cur.execute(sql, tupl)
                    conn.commit()
                    break

                num += 1
        

    return


# EXPORT YOUR SESSION ID COOKIE AS AN ENVIRONMENT VARIABLE CALLED COOKIE
    # cookies_dict = {"sessionid": os.environ.get("COOKIE")}
    # url = "https://atlas.ai.umich.edu/course/EECS%20201/"
    # user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    # resp = requests.get(url, headers={'user-agent': user_agent}, timeout=15.0, cookies=cookies_dict)
    # soup = BeautifulSoup(resp.content, features="html.parser")
    # span = soup.find("span", {"class": "course-credit-label"})
    # credit = span.text
    # credit = credit.split()
    # credit_hours = int(float(credit[0]))
    # workload = soup.find("evaluation-card", {"class-prefix": "workload"})
    # workload = int(float(workload.get(":value")))


if __name__ == "__main__":
    main()