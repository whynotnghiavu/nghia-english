import csv
import requests
from bs4 import BeautifulSoup
# # from urllib.parse import urlparse, urljoin

links = [
    # "https://downloadlynet.ir/2024/03/113706/01/power-bi-masterclass-8-python-finance-and-advanced-dax/14/?#/113706-udemy-042408072531.html",
    # "https://downloadlynet.ir/2023/10/108484/11/become-a-data-analyst-etl-sql-power-bi-pythonr/13/?#/108484-udemy-042408073231.html",
    # "https://downloadlynet.ir/2023/19/100530/07/become-a-data-analyst-python-excel-sql-power-bi/17/?#/100530-udemy-042408073331.html",
    # "https://downloadlynet.ir/2022/12/84707/09/data-analysts-toolbox-excel-python-power-bi-pivottables/14/?#/84707-udemy-042408073631.html",


"https://downloadlynet.ir/2024/03/113706/01/power-bi-masterclass-8-python-finance-and-advanced-dax/14/?#/113706-udemy-042408072531.html",
"https://downloadlynet.ir/2023/10/108484/11/become-a-data-analyst-etl-sql-power-bi-pythonr/13/?#/108484-udemy-042408073231.html",
"https://downloadlynet.ir/2023/19/100530/07/become-a-data-analyst-python-excel-sql-power-bi/17/?#/100530-udemy-042408073331.html",
"https://downloadlynet.ir/2022/12/84707/09/data-analysts-toolbox-excel-python-power-bi-pivottables/14/?#/84707-udemy-042408073631.html",
"https://downloadlynet.ir/2024/23/129779/06/power-bi-data-visualization-essentials-with-power-bi/23/?#/129779-udemy-042410071531.html",
"https://downloadlynet.ir/2024/30/133478/07/microsoft-power-bi-the-complete-masterclass/15/?#/133478-udemy-042411072831.html",
"https://downloadlynet.ir/2024/13/131566/07/power-bi-power-query-and-dax-skills-test/18/?#/131566-udemy-042411073631.html",
"https://downloadlynet.ir/2024/13/131502/07/chatgpt-and-power-bi/11/?#/131502-linkedin-042411073831.html",
"https://downloadlynet.ir/2024/11/131276/07/from-excel-to-power-bi-2/18/?#/131276-udemy-042411074431.html",
"https://downloadlynet.ir/2024/24/129810/06/power-bi-beginner-to-advance-with-data-analysis-masterclass/06/?#/129810-udemy-042411074431.html",
"https://downloadlynet.ir/2024/24/129807/06/power-bi-essentials-from-data-to-dashboard/06/?#/129807-udemy-042411074431.html",
"https://downloadlynet.ir/2024/24/129804/06/power-bi-mastery-zero-to-hero-data-skills/06/?#/129804-udemy-042411074431.html",
"https://downloadlynet.ir/2024/23/129782/06/power-bi-master-class-data-models-and-dax-formulas/23/?#/129782-udemy-042411074431.html",
"https://downloadlynet.ir/2024/23/129779/06/power-bi-data-visualization-essentials-with-power-bi/23/?#/129779-udemy-042411074431.html",
"https://downloadlynet.ir/2024/22/129640/06/power-bi-data-analytics-essentials-with-power-bi/21/?#/129640-udemy-042411074431.html",
"https://downloadlynet.ir/2024/22/129620/06/power-bi-master-microsoft-power-bi-basic-to-advanced/13/?#/129620-udemy-042411074531.html",
"https://downloadlynet.ir/2024/17/129165/06/power-bi-for-construction-projects-your-first-dashboard/20/?#/129165-udemy-042411075631.html",
"https://downloadlynet.ir/2024/17/129162/06/microsoft-power-bi-for-construction-management/20/?#/129162-udemy-042411075631.html",
"https://downloadlynet.ir/2024/18/126591/05/microsoft-power-bi-tutorial-2024-beginners-professional/22/?#/126591-udemy-042411075631.html",
"https://downloadlynet.ir/2024/16/126433/05/microsoft-power-bi-for-financial-reporting/19/?#/126433-udemy-042411075631.html",
"https://downloadlynet.ir/2024/16/126430/05/power-bi-financial-reporting-financial-analysis-a-to-z/18/?#/126430-udemy-042411075631.html",
"https://downloadlynet.ir/2024/29/124923/04/power-bi-a-beginners-guide-to-visualization-and-analysis/10/?#/124923-udemy-042411075631.html",
"https://downloadlynet.ir/2024/27/124843/04/learn-microsoft-power-bi-in-microsoft-fabric-2-in-1-course/23/?#/124843-udemy-042411075631.html",
"https://downloadlynet.ir/2024/26/124760/04/power-bi-and-bim-analysis-and-visualization/20/?#/124760-linkedin-042411075631.html",
"https://downloadlynet.ir/2024/30/122051/03/power-bi-bootcamp-zero-to-hero-just-5-hours/16/?#/122051-udemy-042411075631.html",
"https://downloadlynet.ir/2021/16/47999/08/power-bi-dashboard-design-video-course/15/?#/47999-sqlbi-042416072831.html",
"https://downloadlynet.ir/2020/20/7598/03/microsoft-power-bi-a-complete-introduction/00/",
"https://downloadlynet.ir/2020/15/5684/03/microsoft-power-bi-up-running-with-power-bi-desktop/21/",
"https://downloadlynet.ir/2020/12/2101/02/power-bi-report-server/03/?#/2101-microsof-042416072831.html",
"https://downloadlynet.ir/2023/19/100530/07/become-a-data-analyst-python-excel-sql-power-bi/17/?#/100530-udemy-042414072131.html",
"https://downloadlynet.ir/2023/20/99087/06/power-bi-business-scenarios-with-hands-on-use-cases/21/?#/99087-udemy-042414072531.html",
"https://downloadlynet.ir/2023/18/98974/06/power-pivoting-microsoft-power-bi-for-career-changers/22/?#/98974-udemy-042414072531.html",
"https://downloadlynet.ir/2023/18/98971/06/power-bi-business-intelligence-for-beginners-to-advance/22/?#/98971-udemy-042414072531.html",
"https://downloadlynet.ir/2023/15/96924/05/primavera-power-bi-integration-interactive-dashboards/22/?#/96924-udemy-042414072531.html",
"https://downloadlynet.ir/2023/10/96597/05/power-bi-dax-masterclass-measures-calculated-columns/18/?#/96597-udemy-042414072531.html",
"https://downloadlynet.ir/2023/07/94903/04/the-complete-power-bi-practical-course-2023/20/?#/94903-udemy-042414073231.html",
"https://downloadlynet.ir/2023/05/94766/04/power-bi-bootcamp-zero-to-mastery/12/?#/94766-zerotoma-042414073231.html",
"https://downloadlynet.ir/2023/08/93105/03/power-bi-data-analytics-course-and-dashboards-creation-2023/21/?#/93105-udemy-042414073231.html",
"https://downloadlynet.ir/2023/03/92797/03/power-bi-bootcamp-build-real-world-power-bi-projects/09/?#/92797-udemy-042414073231.html",
"https://downloadlynet.ir/2023/12/91765/02/microsoft-power-bi-up-running-with-power-bi-service/15/?#/91765-udemy-042414075531.html",
"https://downloadlynet.ir/2023/30/91036/01/microsoft-power-bi-certification-da-100-pl-300-exam-prep/01/",
"https://downloadlynet.ir/2022/19/88725/12/microsoft-power-bi-for-project-planning-and-control/19/",
"https://downloadlynet.ir/2022/13/85676/10/power-bi-master-power-bi-with-40-hours-of-premium-content/02/",
"https://downloadlynet.ir/2022/12/85660/10/pl-300-certification-microsoft-power-bi-data-analyst-da-100/19/",
"https://downloadlynet.ir/2022/12/85657/10/15-days-of-power-bi-complete-microsoft-power-bi-bootcamp/19/",
"https://downloadlynet.ir/2022/05/85417/10/advanced-dax-for-microsoft-power-bi-desktop/20/",
"https://downloadlynet.ir/2022/05/85371/10/complete-power-bi-bootcamp-go-from-zero-to-hero/09/",
"https://downloadlynet.ir/2022/12/84707/09/data-analysts-toolbox-excel-python-power-bi-pivottables/14/",
"https://downloadlynet.ir/2021/23/51287/09/da-100-certification-analyzing-data-with-microsoft-power-bi/14/",
"https://downloadlynet.ir/2024/19/121310/03/microsoft-power-bi-data-modeling-data-manipulation/20/?#/121310-udemy-042412073931.html",
"https://downloadlynet.ir/2024/14/120672/03/microsoft-power-bi-portfolio-in-a-day/19/?#/120672-udemy-042412074131.html",
"https://downloadlynet.ir/2024/13/120534/03/advanced-sql-and-power-bi-for-data-analyst-and-bi-developer/13/?#/120534-udemy-042412074131.html",
"https://downloadlynet.ir/2024/15/117665/02/microsoft-power-bi-a-complete-guide-2023-edition/14/?#/117665-udemy-042412074431.html",
"https://downloadlynet.ir/2024/27/115957/01/from-excel-to-power-bi/23/?#/115957-coursera-042412074531.html",
"https://downloadlynet.ir/2024/06/113932/01/master-power-bi-30-hands-on-projects-for-data-visualization/13/?#/113932-udemy-042412075131.html",
"https://downloadlynet.ir/2024/03/113706/01/power-bi-masterclass-8-python-finance-and-advanced-dax/14/?#/113706-udemy-042412075131.html",
"https://downloadlynet.ir/2023/28/113228/12/microsoft-power-bi-the-art-of-designing-incredible-tools/22/?#/113228-udemy-042412075131.html",
"https://downloadlynet.ir/2023/28/113225/12/mastering-dax-calculations-in-microsoft-power-bi/22/?#/113225-udemy-042412075531.html",
"https://downloadlynet.ir/2023/28/110040/11/data-analysts-toolbox-excel-sql-power-bi/00/?#/110040-udemy-042412075731.html",
"https://downloadlynet.ir/2023/15/109021/11/data-analyst-in-power-bi/22/?#/109021-datacamp-042413072731.html",
"https://downloadlynet.ir/2023/11/108655/11/data-analysis-sqltableaupower-bi-excel-real-projects/21/?#/108655-udemy-042413072731.html",
"https://downloadlynet.ir/2023/10/108484/11/become-a-data-analyst-etl-sql-power-bi-pythonr/13/",
"https://downloadlynet.ir/2023/08/108293/11/exam-da-100-analyzing-data-with-microsoft-power-bi-video/01/",
"https://downloadlynet.ir/2023/10/106477/10/power-bi-masterclass-beginners-to-advanced/22/",
"https://downloadlynet.ir/2023/23/105408/09/microsoft-power-bi-data-analyst-professional-certificate/00/",
"https://downloadlynet.ir/2023/10/102073/08/microsoft-power-bi-desktop-and-dax-plus-dashboard-creation/16/",
"https://downloadlynet.ir/2023/10/102060/08/build-this-modern-ux-ui-designed-power-bi-desktop-report/14/",
"https://downloadlynet.ir/2023/07/101859/08/microsoft-power-bi-desktop-for-business-intelligence-pl300/01/",

    
]


data = []


for link in links:
    print(f"URL: {link}")

    response = requests.get(link)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.title.string.strip() if soup.title else 'No title found'
    print(f"title: {title}")





    a_tags = soup.find_all('a')

    for a in a_tags:
        href = a.get('href')
        if href and href.startswith('https://href.li/?https'):
            print(a)
            url = href.split("https://href.li/?")[1]



    # data.append({"link": link, "title": title, "url": url})
    data.append({"title": title, "url": url})


with open('output.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["link", "title", "url"])
    writer.writeheader()
    writer.writerows(data)

print("Dữ liệu đã được thêm vào file CSV thành công.")

      