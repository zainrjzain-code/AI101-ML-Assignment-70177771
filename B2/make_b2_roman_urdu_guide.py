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
out_dir = r"C:\Users\Hp\.gemini\antigravity\scratch\AI101-ML-Assignment-70177771\B2"
pdf_path = os.path.join(out_dir, "Task_B2_Complete_Project_Guide_Roman_Urdu.pdf")

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
story.append(Paragraph("Task B2: Wine Critic Score Prediction (Wine Reviews)", styles['DocTitle']))
story.append(Paragraph("Mukammal Roman Urdu aur Simple English Project Guide & Viva Preparation Handbook", styles['DocSubTitle']))
story.append(Paragraph("Student: Muhammad Zain-ul-Abideen | Roll No: 70177771 | Section: B | The University of Lahore", styles['AuthorInfo']))
story.append(HRFlowable(width="100%", thickness=1, color=PRIMARY, spaceBefore=0, spaceAfter=8))

# Section 1
story.append(H1("1. Is Project Ka Maqsad Aur Problem Kya Hai? (Problem Statement)"))
story.append(P("Dunya bhar mein wine ki market bohot bari hai. Professional wine critics (jinhe Sommeliers kehte hain) har wine ko chak kar (taste kar k) 100-point scale par ek score dete hain (jo aam tor par 80 se 100 points k darmian hota hai). 90+ points lene wali wine market mein bohot mehangi bikti hai aur uski international value barh jati hai."))
story.append(P("Is project ka maqsad ye hai k ek aisa Machine Learning Regression model banaya jaye jo kisi bhi wine k metadata (price, country, province, grape variety, taster name) aur critic ki tasting description (note) ko parh kar accurately predict kare k is wine ko kitne points milenge."))
story.append(make_callout(
    "Machine Learning terminology mein ye ek <b>Mixed-Modality Supervised Regression</b> problem hai. Hamara target variable continuous number hai: <b>points ∈ [80, 100]</b>. Evaluation metrics hain: <b>MAE (Mean Absolute Error), RMSE, aur R² (Coefficient of Determination)</b>.",
    "Core Concept"
))

# Section 2
story.append(H1("2. Dataset Aur Sab Se Zaroori De-duplication Step"))
story.append(P("Ye dataset Wine Enthusiast magazine ka benchmark dataset hai jisme total <b>129,971 raw reviews</b> the."))
story.append(H2("A. Mandatory De-duplication (Duplicates Khatam Karna Kyun Zaroori Tha?):"))
story.append(P("Raw dataset mein bohot se syndicated reviews the jo bar bar repeat ho rahe the. Hum ne splitting se pehle duplicate descriptions check keen:"))
story.append(B("<b>10,016 exact duplicate reviews (7.71%)</b> ko remove kiya gaya."))
story.append(B("Total clean unique reviews bachay: <b>119,955</b>."))
story.append(make_callout(
    "<b>Agar duplicates remove na karte to kya hota?</b><br/>"
    "Agar hum duplicate reviews na nikalte, to wahi same review training set mein bhi chala jata aur testing set mein bhi chala jata. Is se <b>Data Leakage</b> hoti. Model us review ko pehle hi yad (memorize) kar chuka hota, jis se test score jhoota behtar nazar aata lekin real life mein naye vintage par model fail ho jata.",
    "Important Viva Point"
))

# Section 3
story.append(H1("3. Feature Engineering: Tabular Aur NLP Ko Kaise Combine Kiya?"))
story.append(P("Dataset mein do tarah ka data tha jisko hum ne ColumnTransformer k zariye jora:"))
story.append(B("<b>1. Structured Metadata Features (108 dimensions):</b>"))
story.append(B("• <i>log(1 + price):</i> Wine ki price $4 se $3,300 tak thi (bohot right-skewed). Hum ne log transform lagaya ta k price normally distributed ho jaye."))
story.append(B("• <i>Missing Price Imputation:</i> Jin reviews mein price missing thi, wahan hum ne training set ka <b>Median ($25.00)</b> fill kiya aur ek binary flag (price_missing) shamil kiya."))
story.append(B("• <i>Categorical Top-20 Grouping:</i> Country, Province, Variety, Winery, aur Taster Name k top 20 categories ko rakha aur baqi sab ko 'Other' mein daal kar One-Hot Encoding ki."))
story.append(B("<b>2. Text Features (15,000 dimensions):</b> Critic ki likhi hui tasting description ko clean kar k <b>TF-IDF Vectorizer</b> se 1-word aur 2-word n-grams extract kiye."))
story.append(B("<b>Combined Matrix:</b> Dono modalities ko combine kar k 15,108 features ka sparse matrix banaya."))

# Page Break for clean reading
story.append(PageBreak())

# Section 4
story.append(H1("4. Data Splitting Aur Zero Leakage Pipeline"))
story.append(P("De-duplication k baad hum ne dataset ko <b>80% Train (95,963 reviews)</b>, <b>10% Validation (11,996 reviews)</b>, aur <b>10% Test (11,996 reviews)</b> mein divide kiya:"))
story.append(B("Median price calculation ($25.00) sirf training set se nikali gayi."))
story.append(B("TF-IDF vocabulary aur StandardScaler sirf training split par fit kiya gaya ta k testing data leak na ho."))

# Section 5
story.append(H1("5. Models Ka Muqabla Aur Validation Alpha Tuning"))
story.append(P("Validation set par hum ne Ridge Regression ka regularization parameter alpha tune kiya (alpha=5.0 sab se best raha). Unseen Test set (11,996 reviews) par sab models ka muqabla darj zail hai:"))

table_headers = ["Model Architecture", "Test MAE", "Test RMSE", "Test R² Score", "Performance Summary"]
table_data = [
    ["Mean Baseline (Dummy)", "2.522 pts", "3.070 pts", "-0.0000", "Har sample ko mean (88.44) predict karta hai"],
    ["SGDRegressor (Squared)", "1.255 pts", "1.596 pts", "0.7300", "Gradient descent linear regression"],
    ["Ridge Regression (α=5.0) *WINNER*", "1.164 pts", "1.476 pts", "0.7689", "76.89% variance accurately explain karta hai"]
]
story.append(make_table(table_headers, table_data, [1.8*inch, 1.0*inch, 1.0*inch, 1.1*inch, 1.9*inch]))
story.append(Spacer(1, 4))
story.append(make_callout(
    "<b>Winner Model: Ridge Regression (Combined Features, alpha = 5.0)</b><br/>"
    "Ridge regression ne <b>R² = 0.7689 (76.89%)</b> aur <b>MAE = 1.164 points</b> deliver kiya. "
    "Iska matlab hai k model ka average prediction error sirf taqreeban 1.1 point hai (maslan 90-point wine ko 89 ya 91 predict karta hai). "
    "Ye dummy baseline (2.522 MAE) se 53.8% behtar hai.",
    "Result Analysis"
))

# Section 6: Mandatory Modality Ablation Study
story.append(H1("6. Mandatory Modality Ablation Study (Bohat Zaroori Tajruba)"))
story.append(P("Assignment ka strict rule tha k hum Ridge regression ko 3 tarah se test karein: (i) Sirf Metadata, (ii) Sirf Text, aur (iii) Dono mila kar:"))

ab_headers = ["Modality Setting", "Test MAE", "Test RMSE", "Test R² Score", "R² Improvement"]
ab_data = [
    ["1. Metadata Only (Price + Origin)", "1.572 pts", "1.990 pts", "0.5800 (58.0%)", "Baseline"],
    ["2. Text Only (Tasting Note TF-IDF)", "1.351 pts", "1.715 pts", "0.6879 (68.8%)", "+10.79% over Metadata"],
    ["3. Combined (Metadata + Text)", "1.164 pts", "1.476 pts", "0.7689 (76.9%)", "+18.89% over Metadata!"]
]
story.append(make_table(ab_headers, ab_data, [2.2*inch, 1.0*inch, 1.0*inch, 1.2*inch, 1.4*inch]))
story.append(Spacer(1, 4))
story.append(P("<b>Ablation Se Kya Pata Chala? (Answer to Assignment Question 1):</b>"))
story.append(P("Jab hum ne sirf price aur origin metadata use kiya to R² 0.5800 mila. Kyunki mehangi wines aam tor par behtar hoti hain (price aur points ka correlation +0.61 hai). Lekin jab hum ne sommelier ki likhi hui tasting note shamil ki, to model ki accuracy seedhi <b>58.0% se chalang laga kar 76.89% (+18.89% gain)</b> ho gayi!"))
story.append(P("Is se sabit hota hai k wine ka taste aur description parhna bohot zaroori hai, kyunki ek $80 ki bottle bohot shandar 96-point wine bhi ho sakti hai aur kharab 86-point wine bhi."))

# Page Break for clean reading
story.append(PageBreak())

# Section 7: Assignment Specific Questions
story.append(H1("7. Assignment K 4 Sawalat K Detailed Jawabat"))

story.append(H2("Sawal 1: Tasting note price aur origin se aagay kitna faida deti hai?"))
story.append(P("<b>Jawab:</b> Tasting note model ki accuracy mein <b>+18.89% R² ka zabardast izafa karti hai</b> (0.5800 se barh kar 0.7689) aur har bottle par average error ko 1.572 se kam kar k 1.164 points par le aati hai."))

story.append(H2("Sawal 2: Kaun se alfaz (words) score ko oopar ya neechay dhakelte hain? (Ridge Coefficients)"))
story.append(P("<b>1. Score Oopar Le Jane Waley Alfaz (Positive Words - Shandar Quality):</b> <i>layered</i> (+0.54), <i>seamless</i> (+0.51), <i>cellar</i> (+0.48), <i>long finish</i> (+0.45), <i>opulent</i>, <i>velvety</i>, <i>complex</i>, aur <i>magnificent</i>. Ye alfaz zahir karte hain k wine bohot mature, balance aur lambey arsay tak store karne k qabil hai."))
story.append(P("<b>2. Score Neechay Girane Waley Alfaz (Negative Words - Kharabi ya Saadgi):</b> <i>simple</i> (-0.56), <i>sour</i> (-0.49), <i>green</i> (-0.44), <i>dilute</i> (-0.41), <i>unripe</i>, <i>thin</i>, <i>harsh</i>, aur <i>watery</i>. Ye alfaz kachey angoor, badmaza khatas, aur halkay taste ki nishandahi karte hain."))

story.append(H2("Sawal 3: Extremes (80-82 aur 95+ points) mein prediction sab se kharab kyun hoti hai? Explain Regression to the Mean."))
story.append(P("Hum ne 4 score bands mein error check kiya:"))
story.append(B("<b>80–84 Band (Low):</b> MAE = 1.441 points"))
story.append(B("<b>85–89 Band (Middle / Mean):</b> MAE = <b>1.027 points (Sab se behtareen prediction!)</b>"))
story.append(B("<b>90–94 Band (High):</b> MAE = 1.239 points"))
story.append(B("<b>95–100 Band (Extreme High):</b> MAE = <b>2.048 points (Sab se zyada error!)</b>"))
story.append(P("<b>Waja (Regression to the Mean & L2 Shrinkage):</b>"))
story.append(P("1. Dataset mein 85 se 89 points wali wines 52% se zyada hain (ratings average 88.44 k gird ghoomti hain). Bohat kamzor (80-82) ya world-class (95+) wines bohot rare hoti hain."))
story.append(P("2. Ridge regression L2 penalty lagata hai jo weights ko shrink karta hai ta k overall squared error kam ho. Nateeja ye hota hai k model extreme values ko average ki taraf kheenchtata hai: maslan 98-point wine ko 92 predict karega aur 80-point wine ko 84 predict karega. Is statistical effect ko <b>Regression to the Mean</b> kehte hain."))

story.append(H2("Sawal 4: De-duplication na karne se test score par kya asar parta aur kyun?"))
story.append(P("<b>Jawab:</b> Dataset mein 10,016 duplicate reviews the. Agar hum unhe drop na karte, to wahi exact words train aur test dono mein chale jate. Model unseen wine test karne k bajaye training memory se jawab de deta, jis se test score jhoota behtar lagta. Naye data par jate hi model fail ho jata."))

# Section 8: Top 10 Viva Questions
story.append(H1("8. Instructor Viva Questions & Answers (Tayari K Liye)"))
story.append(P("Agar teacher aap se viva mein sawal poochen to unhe bohot confident aur simple tareeqe se ye explain karein:"))

viva_qa = [
    ("Q1: Aap ne is project mein kaun si problem solve ki?", 
     "Sir, hum ne Wine Reviews dataset par bottle metadata (price, origin, variety) aur critic ki tasting notes k zariye wine k points (80-100) predict karne ka Mixed-Modality Regression model banaya hai."),
    
    ("Q2: Sab se pehla zaroori step kya tha?", 
     "Sir, de-duplication sab se pehla zaroori step tha. Dataset mein 10,016 duplicate reviews the (7.7%). Agar unhe na nikaalte to train aur test k darmian data leak ho jata."),
    
    ("Q3: Kaun sa model winner raha aur kya score diya?", 
     "Sir, Ridge Regression (alpha=5.0) winner raha jisne Test Set par R² = 0.7689 (76.89%), MAE = 1.164 points aur RMSE = 1.476 points deliver kiya."),
    
    ("Q4: Price ko seedha use kyun nahi kiya, log(price) kyun banaya?", 
     "Sir, price mein bohot zyada skewness thi ($4 se $3,300 tak). log(1 + price) karne se price normal bell curve jaisi ban gayi jis se linear model ki correlation aur stability bohot behtar ho gayi."),
    
    ("Q5: Missing price ko kaise handle kiya?", 
     "Sir, hum ne training set ka median price ($25.00) impute kiya aur ek binary flag (price_missing) shamil kiya ta k model ko pata chal sake k kahan price mojood nahi thi."),
    
    ("Q6: Ablation study ka kya nateeja nikla?", 
     "Sir, sirf metadata par R² 0.5800 tha, lekin tasting note shamil karne se R² seedha barh kar 0.7689 ho gaya (+18.89% ka zabardast jump)."),
    
    ("Q7: Kaun se alfaz wine ka score oopar le kar jate hain?", 
     "Sir, 'layered', 'seamless', 'cellar', 'opulent', aur 'long finish' jaise words high positive coefficients show karte hain jo premium quality ki pehchan hain."),
    
    ("Q8: Kaun se alfaz wine ka score gira dete hain?", 
     "Sir, 'simple', 'sour', 'green', 'dilute', aur 'thin' negative coefficients dete hain jo wine ki kharabi ko zahir karte hain."),
    
    ("Q9: Extremes (95-100 points) par error zyada kyun aya?", 
     "Sir, Regression to the Mean aur Ridge L2 Shrinkage ki waja se. Ratings average 88.44 par centered hain, is liye model extreme ratings ko center ki taraf pull karta hai."),
    
    ("Q10: Commercial application kya hai?", 
     "Sir, wine auction houses aur retail stores naye vintages ki description aur pricing dekh kar unka predicted sommelier score pehle se estimate kar sakte hain.")
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
