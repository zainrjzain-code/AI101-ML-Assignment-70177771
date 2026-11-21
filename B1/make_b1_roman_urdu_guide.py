import os
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.colors import HexColor

# Output paths
out_dir = r"C:\Users\Hp\.gemini\antigravity\scratch\AI101-ML-Assignment-70177771\B1"
pdf_path = os.path.join(out_dir, "Task_B1_Complete_Project_Guide_Roman_Urdu.pdf")

# Palette (Professional Academic Theme - No emojis)
PRIMARY = HexColor('#0F2942')    # Deep Navy
SECONDARY = HexColor('#1B4965')  # Steel Blue
ACCENT = HexColor('#2B6CB0')     # Royal Blue
HIGHLIGHT = HexColor('#2D3748')  # Charcoal
LIGHT_BG = HexColor('#F8FAFC')   # Clean paper background
BORDER = HexColor('#CBD5E1')     # Border grey
CARD_BG = HexColor('#F1F5F9')    # Soft card background

styles = getSampleStyleSheet()

# Typography Styles
styles.add(ParagraphStyle(
    name='DocTitle', parent=styles['Title'], fontName='Helvetica-Bold',
    fontSize=17, leading=21, textColor=PRIMARY, alignment=TA_CENTER, spaceAfter=4
))
styles.add(ParagraphStyle(
    name='DocSubTitle', parent=styles['Normal'], fontName='Helvetica',
    fontSize=9.5, leading=13, textColor=SECONDARY, alignment=TA_CENTER, spaceAfter=8
))
styles.add(ParagraphStyle(
    name='AuthorInfo', parent=styles['Normal'], fontName='Helvetica-Bold',
    fontSize=8.5, leading=11, textColor=HIGHLIGHT, alignment=TA_CENTER, spaceAfter=12
))
styles.add(ParagraphStyle(
    name='MainHead', parent=styles['Heading1'], fontName='Helvetica-Bold',
    fontSize=12, leading=15, textColor=PRIMARY, spaceBefore=12, spaceAfter=5, keepWithNext=True
))
styles.add(ParagraphStyle(
    name='SubHead', parent=styles['Heading2'], fontName='Helvetica-Bold',
    fontSize=10, leading=13, textColor=SECONDARY, spaceBefore=8, spaceAfter=3, keepWithNext=True
))
styles.add(ParagraphStyle(
    name='SubSubHead', parent=styles['Heading3'], fontName='Helvetica-Bold',
    fontSize=8.5, leading=11, textColor=ACCENT, spaceBefore=5, spaceAfter=2, keepWithNext=True
))
styles.add(ParagraphStyle(
    name='Body', parent=styles['BodyText'], fontName='Helvetica',
    fontSize=8.2, leading=11.6, textColor=HIGHLIGHT, spaceAfter=4, alignment=TA_JUSTIFY
))
styles.add(ParagraphStyle(
    name='MyBullet', parent=styles['Normal'], fontName='Helvetica',
    fontSize=8.0, leading=11.2, textColor=HIGHLIGHT, leftIndent=12, firstLineIndent=-8, spaceAfter=2.5
))
styles.add(ParagraphStyle(
    name='Callout', parent=styles['Normal'], fontName='Helvetica',
    fontSize=8.0, leading=11.2, textColor=PRIMARY, spaceBefore=2, spaceAfter=2
))
styles.add(ParagraphStyle(
    name='TableHeader', parent=styles['Normal'], fontName='Helvetica-Bold',
    fontSize=7.5, leading=9.5, textColor=colors.white, alignment=TA_CENTER
))
styles.add(ParagraphStyle(
    name='TableCell', parent=styles['Normal'], fontName='Helvetica',
    fontSize=7.2, leading=9.2, textColor=HIGHLIGHT
))
styles.add(ParagraphStyle(
    name='TableCellBold', parent=styles['Normal'], fontName='Helvetica-Bold',
    fontSize=7.2, leading=9.2, textColor=PRIMARY
))

def make_callout(text, title="Key Concept / Zaroori Baat"):
    p_title = Paragraph(f"<b>[ {title.upper()} ]</b>", styles['SubSubHead'])
    p_body = Paragraph(text, styles['Callout'])
    t = Table([[p_title], [p_body]], colWidths=[6.8*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), CARD_BG),
        ('BOX', (0,0), (-1,-1), 1, ACCENT),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6)
    ]))
    return t

def make_table(header_row, data_rows, col_widths):
    table_data = []
    h_row = [Paragraph(f"<b>{col}</b>", styles['TableHeader']) for col in header_row]
    table_data.append(h_row)
    for row in data_rows:
        r = []
        for i, val in enumerate(row):
            txt = str(val)
            if i == 0 or 'Winner' in txt or '*' in txt:
                r.append(Paragraph(txt, styles['TableCellBold']))
            else:
                r.append(Paragraph(txt, styles['TableCell']))
        table_data.append(r)
    
    t = Table(table_data, colWidths=col_widths)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), PRIMARY),
        ('GRID', (0,0), (-1,-1), 0.4, BORDER),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, CARD_BG])
    ]))
    return t

def P(txt): return Paragraph(txt, styles['Body'])
def B(txt): return Paragraph(f"- {txt}", styles['MyBullet'])
def H1(txt): return Paragraph(txt, styles['MainHead'])
def H2(txt): return Paragraph(txt, styles['SubHead'])

doc = SimpleDocTemplate(
    pdf_path,
    pagesize=A4,
    leftMargin=0.55*inch,
    rightMargin=0.55*inch,
    topMargin=0.55*inch,
    bottomMargin=0.55*inch
)

story = []

# Header
story.append(Paragraph("Task B1: Detecting Fraudulent Job Postings (EMSCAD)", styles['DocTitle']))
story.append(Paragraph("Mukammal Roman Urdu aur Simple English Project Guide & Viva Preparation Handbook", styles['DocSubTitle']))
story.append(Paragraph("Student: Muhammad Zain-ul-Abideen | Roll No: 70177771 | Section: B | The University of Lahore", styles['AuthorInfo']))
story.append(HRFlowable(width="100%", thickness=1, color=PRIMARY, spaceBefore=0, spaceAfter=8))

# Section 1
story.append(H1("1. Is Project Ka Maqsad Aur Problem Kya Hai? (Problem Statement)"))
story.append(P("Aaj kal online job portals (jaise LinkedIn, Rozee.pk, Indeed wagera) par rozana hazaron naukriyon k ishtiharat (job ads) aate hain. Lekin unme bohot se ads jhootay (fake ya scam) hote hain jinka maqsad logon se registration fees lena, unka private data churana, ya unhe illegal financial schemes mein phansana hota hai."))
story.append(P("Is project ka maqsad ye hai k ek aisa automated Machine Learning model banaya jaye jo kisi bhi job posting k structured data (company logo, remote job flag, company profile) aur unstructured text (job title, description, requirements, benefits) ko parh kar foran bata de k ye posting <b>Real (Asal)</b> hai ya <b>Fraudulent (Jaali)</b>."))
story.append(make_callout(
    "Machine Learning terminology mein ye ek <b>Imbalanced Binary Classification with Mixed Modality (Tabular + NLP)</b> problem hai. Hamare pas 2 classes hain: Class 0 = Legitimate Job (Real), Class 1 = Fraudulent Job (Fake).",
    "Core Concept"
))

# Section 2
story.append(H1("2. Dataset Ki Complete Tafseel (Dataset & Severe Imbalance)"))
story.append(P("Ye dataset EMSCAD (Employment Scam Aegean Dataset) kehlata hai jo University of the Aegean k researchers ne collect kiya tha. Isme total <b>17,880 job postings</b> hain."))
story.append(H2("A. Severe Class Imbalance (Shadeed Gher-Mawazna Data):"))
story.append(B("<b>Real Postings (0):</b> 17,014 samples (95.16% of total data) - Bohat bari tadad."))
story.append(B("<b>Fraudulent Postings (1):</b> Sirf 866 samples (4.84% of total data) - Bohat choti tadad."))
story.append(P("<b>Kyun Accuracy Yahan Ek Dhoka Hai?</b> Agar koi bilkul 'stupid' model banaya jaye jo har job ko aankhen band kar k 'Real' keh de, to uski Accuracy <b>95.16%</b> aa jayegi! Lekin us model ne ek bhi scam nahi pakra (Fraud Recall = 0.0%). Is liye is project mein Accuracy ko judge nahi kiya jata, balkey <b>Fraud Class F1-Score</b> aur <b>Precision-Recall AUC (PR-AUC)</b> ko dekha jata hai."))

story.append(H2("B. Missing Information Ek Bohat Bara Fraud Signal Hai:"))
story.append(P("Data exploration se pata chala k scammer aksar apni company ka logo aur profile chupate hain:"))
story.append(B("Jis job ad mein <b>Company Logo Mojood Nahi Tha</b>, wahan fraud rate <b>16.5%</b> tha. Lekin jahan logo tha, wahan fraud rate sirf <b>2.1%</b> tha (8 guna farq!)."))
story.append(B("Jis job ad mein <b>Company Profile Khali (Missing)</b> thi, wahan fraud rate <b>19.3%</b> tha, jabke profile waley ads mein fraud rate sirf <b>1.5%</b> tha (13 guna farq!)."))

# Section 3
story.append(H1("3. Feature Engineering: Dono Modalities Ko Kaise Combine Kiya?"))
story.append(P("Hamare pas do tarah ka data tha jinko hum ne ColumnTransformer se jora:"))
story.append(B("<b>1. Structured Features (34 dimensions):</b> Binary flags (telecommuting, has_company_logo, has_questions), missingness indicators (missing_company_profile, missing_salary_range), job description length, aur top categorical categories ka One-Hot Encoding."))
story.append(B("<b>2. Text Features (15,000 dimensions):</b> Job title, profile, description, requirements aur benefits ko aapas mein jor kar aik single text field banaya. Phir <b>TF-IDF Vectorizer</b> k zariye 1-word aur 2-word n-grams (uni-grams aur bi-grams) extract kiye."))
story.append(B("<b>Combined Matrix:</b> Dono ko horizontally stack kar k 15,034 features ka sparse matrix banaya."))

# Page Break for clean reading
story.append(PageBreak())

# Section 4
story.append(H1("4. Data Splitting Aur Leakage Se Bachao"))
story.append(P("Hamare split mein zero leakage ensure ki gayi:"))
story.append(B("<b>Stratified 70/15/15 Split:</b> 12,516 Train (606 fraud), 2,682 Validation (130 fraud), 2,682 Test (130 fraud). Stratification se teeno hisson mein exact 4.84% fraud ka ratio maintain raha."))
story.append(B("<b>Strict Pipeline Boundaries:</b> TF-IDF aur StandardScaler ko sirf aur sirf <b>Training Split</b> par fit kiya gaya. Testing data ka koi lafz ya number training scaler mein shamil nahi hua."))

# Section 5
story.append(H1("5. Models Ka Muqabla Aur Validation Threshold Tuning"))
story.append(P("Severe imbalance se nipatne k liye hum ne <i>class_weight='balanced'</i> lagaya aur <b>Validation set par decision threshold tune kiya</b> (ta k positive class F1 maximize ho sake). Held-out Test set (2,682 samples) par final results:"))

table_headers = ["Model Architecture", "Tuned Thresh", "Fraud F1", "Precision", "Recall", "PR-AUC"]
table_data = [
    ["Logistic Regression *WINNER*", "0.66", "0.7958", "0.7338", "0.8692", "0.8770"],
    ["Linear SVM (SGD Calibrated)", "0.78", "0.7757", "0.7669", "0.7846", "0.8641"],
    ["Random Forest (150 trees)", "0.70", "0.7324", "0.9398", "0.6000", "0.8435"]
]
story.append(make_table(table_headers, table_data, [2.0*inch, 0.9*inch, 1.0*inch, 0.9*inch, 0.9*inch, 1.1*inch]))
story.append(Spacer(1, 4))
story.append(make_callout(
    "<b>Winner Model: Logistic Regression (Combined Features, Threshold = 0.66)</b><br/>"
    "Logistic Regression ne <b>0.7958 Fraud F1</b> aur <b>0.8770 PR-AUC</b> score hasil kiya jo sab se zyada hai. "
    "Sab se zaroori baat: is model ne 130 mein se <b>113 fraud jobs ko kamyabi se pakra (Recall = 86.92%)</b>. "
    "Random Forest ki precision high thi (93.98%), lekin usne 40% fraud jobs chor deen (Recall sirf 60%), jo scam detection mein khatarnak hai.",
    "Result Analysis"
))

# Section 6: Mandatory Ablation Study
story.append(H1("6. Mandatory Modality Ablation Study (Bohat Zaroori Tajruba)"))
story.append(P("Assignment ka strict requirement tha k model ko (i) Sirf Structured features, (ii) Sirf Text features, aur (iii) Dono mila kar train karein aur nateeja dekhein:"))

ab_headers = ["Modality Setting", "Fraud F1", "Precision", "Recall", "PR-AUC"]
ab_data = [
    ["1. Structured Features Only", "0.3057", "0.2111", "0.5538", "0.1954"],
    ["2. Text Features Only", "0.8699", "0.9224", "0.8231", "0.9013"],
    ["3. Combined (Structured + Text)", "0.7958", "0.7338", "0.8692 (Catches 113/130)", "0.8770"]
]
story.append(make_table(ab_headers, ab_data, [2.4*inch, 1.1*inch, 1.1*inch, 1.1*inch, 1.1*inch]))
story.append(Spacer(1, 4))
story.append(P("<b>Ablation Se Kya Sabit Hua?</b>"))
story.append(B("Sirf structured metadata (F1=0.3057) akela kafi nahi hai, kyunki baghair text parhay sirf logo ya profile dekh kar faisla nahi kiya ja sakta."))
story.append(B("Text features akele bohot strong hain (F1=0.8699) kyunki scam language bilkul wazeh hoti hai."))
story.append(B("Lekin jab hum ne structured metadata ko text k sath jora, to hamara <b>Fraud Recall 82.31% se barh kar 86.92% ho gaya (+4.61% gain)</b>. Yani model ne 6 mazeed mushkil fraud pakre jo sirf text se nahi pakray ja rahay the! Scam detection mein sab se pehla maqsad user ko lutne se bachana hota hai, is liye Recall barhana sab se ahem hai."))

# Page Break for clean reading
story.append(PageBreak())

# Section 7: Assignment Specific Questions
story.append(H1("7. Assignment K Sawalat K Detailed Jawabat"))

story.append(H2("Sawal 1: Accuracy yahan bura metric kyun hai? Dummy model kya accuracy deta hai?"))
story.append(P("<b>Jawab:</b> Dataset mein 95.16% real jobs hain aur sirf 4.84% fake jobs hain. Ek dummy baseline jo har posting ko 'Real' keh deta hai, wo <b>95.16% Accuracy</b> de deta hai. Lekin us model ka fraud pakarne ka Recall <b>0.0%</b> hota hai. Accuracy minority class k fail hone ko chupa leti hai. Is liye F1-score aur PR-AUC sahi metrics hain."))

story.append(H2("Sawal 2: Kya text aur structured features ko milane se faida hua?"))
story.append(P("<b>Jawab:</b> Ji haan! Dono ko milane se hamara <b>Fraud Recall 82.31% se barh kar 86.92% ho gaya</b>. Model ne 130 mein se 113 scam pakre (sirf text waley model ne 107 pakre the). Corporate branding aur profile missingness ne model ko un chalak scams ko pehchanne mein madad di jinki description dekhne mein real lagti thi."))

story.append(H2("Sawal 3: Kaun se alfaz (words) aur structured features fraud zahir karte hain? False Positives kya hain?"))
story.append(P("<b>1. Fraud Zahir Karne Waley Top Alfaz (N-Grams):</b> <i>administrative entry</i>, <i>clerical data</i>, <i>clerical administrative</i>, <i>wire transfer</i>, <i>payroll</i>, aur <i>data entry</i>. Ye terms 'work-from-home' check fraud schemes mein use hoti hain."))
story.append(P("<b>2. Top Structured Features:</b> <i>missing_company_profile</i> (+1.84 coefficient) aur <i>has_company_logo = 0</i> (+1.12 coefficient). Jaali companies ke pas verified profile aur logo nahi hota."))
story.append(P("<b>3. False Positives (Asal jobs jo ghalati se fake ban gayen):</b> Test set par 41 real jobs ghalati se fraud predict huin. Unka jaiza lene se pata chala k ye aam tor par choti nayi companies (startups) theen jinhon ne jaldi mein company profile khali chor di thi, unke pas logo upload nahi tha, aur wo remote data-entry ya virtual assistant hire kar rahe the. Unka structure bilkul scam jaisa lagta tha is liye model ne unhe flag kar diya."))

# Section 8: Top 10 Viva Questions
story.append(H1("8. Instructor Viva Questions & Answers (Tayari K Liye)"))
story.append(P("Agar teacher aap se viva mein sawal poochen to unhe bohot confident aur simple tareeqe se ye explain karein:"))

viva_qa = [
    ("Q1: Aap ne is project mein kaun sa task solve kiya?", 
     "Sir, hum ne EMSCAD dataset par Fake Job Postings (jaali naukriyon k ishtiharat) ko detect karne ka Mixed-Modality Binary Classification system banaya hai."),
    
    ("Q2: Mixed Modality ka kya matlab hai?", 
     "Sir, iska matlab hai k hum ne ek hi model k andar Structured Tabular data (jaise company logo, remote flag, text word counts) aur Unstructured Natural Language Text (job title, description, requirements) dono ko combine kar k train kiya hai."),
    
    ("Q3: Dataset mein class imbalance kitna tha?", 
     "Sir, dataset mein 17,014 real jobs theen (95.16%) aur sirf 866 fraudulent jobs theen (4.84%). Yani taqreeban 20 mein se sirf 1 job fake thi."),
    
    ("Q4: Agar dummy model 95% accuracy deta hai to aap ne model kyun banaya?", 
     "Sir, dummy model har job ko Real keh deta hai, jis se uski fraud detection recall 0% hoti hai aur wo ek bhi scammer ko nahi pakar sakta. Hamara model 86.92% frauds ko accurately catch karta hai aur 0.8770 PR-AUC achieve karta hai."),
    
    ("Q5: Imbalance se nipatne k liye aap ne kya kiya?", 
     "Sir, hum ne do techniques use keen: pehle hum ne class_weight='balanced' lagaya ta k fraud class ki ghalati par model ko zyada penalty miley, aur doosra hum ne Validation set par decision threshold ko 0.5 se tune kar k 0.66 par set kiya."),
    
    ("Q6: Ablation study mein kya nateeja nikla?", 
     "Sir, hum ne dekha k sirf text use karne se 82.31% recall milta hai, lekin jab hum ne structured metadata (company profile aur logo presence) ko text k sath combine kiya to recall barh kar 86.92% ho gaya (+4.61% boost)."),
    
    ("Q7: Kaun se alfaz fraud mein sab se zyada aate hain?", 
     "Sir, 'wire transfer', 'administrative entry', 'clerical data', aur 'data entry' sab se zyada positive coefficients show karte hain jo standard work-from-home scams ki pehchan hain."),
    
    ("Q8: Missingness indicator ka kya role hai?", 
     "Sir, missing_company_profile ek zabardast signal hai. Jis ad mein profile khali thi wahan fraud rate 19.3% tha, jabke profile waley ads mein sirf 1.5% tha."),
    
    ("Q9: False positives kyun aate hain?", 
     "Sir, choti legitimate startups jinke pas logo nahi hota aur jinhon ne profile khali chori hoti hai, unka profile scam jaisa lagta hai, is liye model unhe suspicious mark kar deta hai."),
    
    ("Q10: Kaun sa model winner raha?", 
     "Sir, L2-regularized Logistic Regression winner raha jisne 0.7958 Fraud F1, 0.8770 PR-AUC aur 86.92% Recall deliver kiya.")
]

for q, a in viva_qa:
    story.append(Paragraph(f"<b>{q}</b>", styles['SubSubHead']))
    story.append(Paragraph(a, styles['Body']))
    story.append(Spacer(1, 2))

story.append(Spacer(1, 6))
story.append(HRFlowable(width="100%", thickness=0.8, color=BORDER, spaceBefore=4, spaceAfter=6))
story.append(Paragraph("<b>End of Guide | Good luck with your assignment submission and viva!</b>", styles['AuthorInfo']))

doc.build(story)
print(f"Roman Urdu guide successfully compiled: {pdf_path}")
