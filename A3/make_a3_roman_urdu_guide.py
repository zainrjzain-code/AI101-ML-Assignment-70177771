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
out_dir = r"C:\Users\Hp\.gemini\antigravity\scratch\AI101-ML-Assignment-70177771\A3"
pdf_path = os.path.join(out_dir, "Task_A3_Complete_Project_Guide_Roman_Urdu.pdf")

# Palette (Professional Academic Theme - No emojis)
PRIMARY = HexColor('#0F2942')    # Deep Navy
SECONDARY = HexColor('#1B4965')  # Steel Blue
ACCENT = HexColor('#2B6CB0')     # Royal Blue
HIGHLIGHT = HexColor('#2D3748')  # Charcoal
LIGHT_BG = HexColor('#F8FAFC')   # Clean paper background
BORDER = HexColor('#CBD5E1')     # Border grey
CARD_BG = HexColor('#F1F5F9')    # Soft card background
SUCCESS = HexColor('#1E3A8A')

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
story.append(Paragraph("Task A3: Dry Bean Variety Multi-Class Classification", styles['DocTitle']))
story.append(Paragraph("Mukammal Roman Urdu aur Simple English Project Guide & Viva Preparation Handbook", styles['DocSubTitle']))
story.append(Paragraph("Student: Muhammad Zain-ul-Abideen | Roll No: 70177771 | Section: B | The University of Lahore", styles['AuthorInfo']))
story.append(HRFlowable(width="100%", thickness=1, color=PRIMARY, spaceBefore=0, spaceAfter=8))

# Section 1
story.append(H1("1. Is Project Ka Maqsad Aur Problem Kya Hai? (Problem Statement)"))
story.append(P("Is project ka maqsad ye hai k computer vision se extract kiye gaye 16 geometric aur shape features ki madad se khushk lobia (Dry Beans) ko unki 7 mukhtalif registered varieties mein accurately classify kiya jaye."))
story.append(P("Kisan (farmers), seed processing mills aur export companies k liye har lobia ki variety ko alag pehchanna bohot zaroori hota hai, kyunki har variety ki market price, pakane ka waqt (cooking time), aur ugne ki salahiyat (germination rate) mukhtalif hoti hai. Agar insan hath se ek ek dana check kare to bohot waqt lagta hai aur ghalati ka imkan bohot zyada hota hai. Is liye Machine Learning algorithm use kar k is poore process ko automatic banaya gaya hai."))
story.append(make_callout(
    "Machine Learning terminology mein ye ek <b>Multi-Class Supervised Classification</b> problem hai. Hamare pas total 7 classes hain: <b>Dermason, Sira, Seker, Horoz, Cali, Barbunya, aur Bombay</b>. Har sample k 16 continuous numerical features hain.",
    "Core Concept"
))

# Section 2
story.append(H1("2. Dataset Ki Complete Tafseel (Dataset & Features)"))
story.append(P("Ye dataset UCI Machine Learning Repository se liya gaya hai jisme total <b>13,611 bean samples</b> hain. Dataset mein koi bhi missing value (null) nahi thi."))
story.append(H2("A. 7 Bean Varieties (Classes) Ki Tadaad:"))
story.append(B("<b>Dermason:</b> 3,546 samples (26.05%) - Sab se bari class"))
story.append(B("<b>Sira:</b> 2,636 samples (19.37%)"))
story.append(B("<b>Seker:</b> 2,027 samples (14.89%) - Gol (round) shape waley beans"))
story.append(B("<b>Horoz:</b> 1,928 samples (14.16%) - Lambey (elongated) shape waley beans"))
story.append(B("<b>Cali:</b> 1,630 samples (11.98%)"))
story.append(B("<b>Barbunya:</b> 1,322 samples (9.71%)"))
story.append(B("<b>Bombay:</b> 522 samples (3.84%) - Sab se choti class, lekin size mein sab se bara dana"))
story.append(P("<b>Class Imbalance:</b> Dermason aur Bombay k darmian taqreeban 6.8:1 ka farq hai. Yani Dermason Bombay se 6.8 guna zyada hai. Is liye hum ne model ko judge karne k liye sirf Accuracy nahi dekhi, balkey <b>Macro-Averaged F1-score</b> ko primary metric banaya ta k choti class (Bombay) ko bhi barabar ahmiyat miley."))

story.append(H2("B. 16 Input Features Kya Hain?"))
story.append(P("Features ko 2 baray hisson mein divide kiya gaya hai:"))
story.append(B("<b>12 Geometric Features (Size aur Dimensions):</b> Area (total pixels), Perimeter (boundary length), MajorAxisLength (lambai), MinorAxisLength (chorai), AspectRatio (lambai / chorai), Eccentricity (golai se kitna hat kar hai), ConvexArea, EquivDiameter, Extent, Solidity, Roundness, aur Compactness."))
story.append(B("<b>4 Shape Factors (ShapeForm Descriptors):</b> ShapeFactor1 se ShapeFactor4 tak. Ye mathematical formulas hain jo bean k curve aur banawat ko describe karte hain."))

# Section 3
story.append(H1("3. Preprocessing Aur Data Leakage Se Bachao (Methodology)"))
story.append(P("Machine Learning mein sab se bari ghalati Data Leakage hoti hai (yani testing data ki information training k waqt model k andar chali jana). Hum ne is se bachne k liye strict best practices follow keen:"))
story.append(B("<b>Stratified 70/15/15 Data Split:</b> Pure dataset ko 70% Training (9,527 samples), 15% Validation (2,042 samples), aur 15% Test (2,042 samples) mein divide kiya. Stratified ka matlab hai k teeno hisson mein har bean variety ki percentage bilkul barabar rakhi gayi."))
story.append(B("<b>Zero Data Leakage Scaling:</b> Features ki values bohot mukhtalif theen (Area 170,000+ tha jabke Compactness 0.7 thi). Is liye StandardScaler se sab features ko mean=0 aur std=1 par normalize kiya. Scaler ko <b>sirf Training set</b> par fit kiya aur usi scaler se Validation aur Test ko transform kiya."))

# Page Break for clean reading
story.append(PageBreak())

# Section 4
story.append(H1("4. Kaun Kaun Se Models Train Kiye Gaye?"))
story.append(P("Assignment ki requirement k mutabiq 5 mukhtalif algorithms ko compare kiya gaya:"))
story.append(B("<b>1. Multinomial Logistic Regression:</b> Softmax function k sath linear baseline model. Fast aur simple."))
story.append(B("<b>2. Support Vector Machine (SVM):</b> Non-linear RBF (Radial Basis Function) kernel k sath. Parameter C=10.0 select kiya jo complex decision boundaries banata hai."))
story.append(B("<b>3. Random Forest:</b> 200 decision trees ka ensemble. Features ki non-linear interactions ko capture karta hai."))
story.append(B("<b>4. Gradient Boosting:</b> 150 sequential boosting trees, learning rate 0.1 k sath. Har naya tree pichle tree ki ghalatiyon ko theek karta hai."))
story.append(B("<b>5. Multi-Layer Perceptron (MLP):</b> Feedforward Deep Neural Network jisme 2 hidden layers theen (128 aur 64 neurons), ReLU activation aur Adam optimizer."))

# Section 5: Comparison Table
story.append(H1("5. Models Ka Muqabla Aur Nateeja (Results & Winner)"))
story.append(P("Held-out Test set (2,042 unseen samples) par sab models ka muqabla darj zail hai:"))

table_headers = ["Model", "Accuracy", "Macro Prec", "Macro Rec", "Macro F1", "Weighted F1"]
table_data = [
    ["Logistic Regression", "92.02%", "0.9329", "0.9332", "0.9327", "0.9201"],
    ["SVM (RBF Kernel) *WINNER*", "92.56%", "0.9372", "0.9355", "0.9360", "0.9252"],
    ["Random Forest (200 trees)", "91.97%", "0.9312", "0.9317", "0.9313", "0.9196"],
    ["Gradient Boosting", "91.63%", "0.9278", "0.9303", "0.9287", "0.9163"],
    ["MLP (128-64 Neural Net)", "92.21%", "0.9351", "0.9331", "0.9338", "0.9218"]
]
story.append(make_table(table_headers, table_data, [1.8*inch, 1.0*inch, 1.0*inch, 1.0*inch, 1.0*inch, 1.0*inch]))
story.append(Spacer(1, 4))
story.append(make_callout(
    "<b>Winner: Support Vector Machine (SVM with RBF kernel)</b><br/>"
    "SVM ne <b>92.56% Accuracy</b> aur <b>0.9360 Macro-F1</b> score hasil kiya jo sab se zyada hai. "
    "Kyunki bean k morphological features smooth geometric curves banate hain, SVM ka RBF kernel high-dimensional space mein smooth non-linear separation boundary banata hai jo decision trees ki orthogonal box splits se behtar perform karta hai.",
    "Result Analysis"
))

# Section 6: Specific Assignment Questions
story.append(H1("6. Assignment K 3 Zaroori Sawalat K Detailed Jawabat"))

story.append(H2("Sawal 1: Kaun si varieties aapas mein sab se zyada confuse hoti hain aur kyun?"))
story.append(P("<b>Jawab:</b> Confusion Matrix ko dekh kar saaf pata chalta hai k <b>Dermason aur Sira</b> aapas mein sab se zyada misclassify hoti hain:"))
story.append(B("38 actual Sira beans ko model ne ghalati se Dermason predict kiya."))
story.append(B("33 actual Dermason beans ko model ne ghalati se Sira predict kiya."))
story.append(P("<b>Waja (Physical Reason):</b> In dono varieties ka physical size aur shape bohot zyada milta julta hai. Dermason ka average area taqreeban 32,118 pixels hai aur Sira ka 44,729 pixels hai. Dono hi medium-sized, elliptical (baizwi) beans hain. Inka aspect ratio, compactness aur shape factors itne qareeb hain k geometric features k zariye inka overlap ho jata hai."))
story.append(P("Is k bar-aks, <b>Bombay variety ko model ne 100% sahi pehchana (Precision=1.0, Recall=1.0)</b>. Bombay ka average area 170,000+ pixels hai jo k baqi sab lobia se 4 se 5 guna bara hai, is liye feature space mein Bombay bilkul akela alag thalag khara nazar aata hai."))

story.append(H2("Sawal 2: Kya class weighting (balanced weights) use karne se minority class ki performance behtar hui?"))
story.append(P("<b>Jawab:</b> Ji haan, class weighting lagane se minority class ki performance behtar hui baghair overall accuracy khoye."))
story.append(P("Jab hum ne <i>class_weight='balanced'</i> lagaya to algorithm ne choti classes (jaise Bombay aur Barbunya) k misclassification par zyada jurmana (penalty) lagaya. Nateeja:"))
story.append(B("SVM Validation Macro-F1: <b>0.9397 se barh kar 0.9409</b> ho gaya (+0.12% improvement)."))
story.append(B("Overall Accuracy bilkul nahi giri (92.61% par mustahkam rahi)."))
story.append(P("Is se sabit hota hai k class weighting ek zero-overhead technique hai jo choti classes k recognition ko boost karti hai."))

# Page Break for clean reading
story.append(PageBreak())

story.append(H2("Sawal 3: PCA (Dimensionality Reduction) mein kitne components chahiyen ta k best Macro-F1 ka 98% barkarar rahay?"))
story.append(P("<b>Jawab:</b> Hum ne PCA (Principal Component Analysis) se feature space ko reduce kar k test kiya:"))

pca_headers = ["k (Components)", "Variance Retained", "Test Accuracy", "Test Macro-F1", "% of Best Macro-F1"]
pca_data = [
    ["k = 2", "81.9%", "0.8663", "0.8732", "93.3%"],
    ["k = 4", "94.8%", "0.8937", "0.8987", "96.0%"],
    ["k = 8 *Target Achieved*", "99.7%", "0.9256", "0.9360", "100.0% (Matches Full Model)"],
    ["k = 16 (All Features)", "100.0%", "0.9256", "0.9360", "100.0%"]
]
story.append(make_table(pca_headers, pca_data, [1.5*inch, 1.4*inch, 1.2*inch, 1.2*inch, 1.5*inch]))
story.append(Spacer(1, 4))
story.append(P("Hamara best Macro-F1 score 0.9360 hai. Is ka 98% banta hai: <b>0.98 × 0.9360 = 0.9173</b>."))
story.append(B("k = 4 components par Macro-F1 0.8987 milta hai jo k 96.0% hai (98% se thora kam hai)."))
story.append(B("k = 8 components par Macro-F1 0.9360 milta hai jo k <b>100% of peak score</b> hai aur 99.7% variance retain karta hai."))
story.append(P("<b>Final Answer: Hamein 8 components ki zaroorat hai.</b> 8 components use karne se hamare 50% features khatam ho jate hain, computation fast ho jati hai, aur accuracy bilkul bhi kam nahi hoti!"))

# Section 7: Top 10 Viva Questions
story.append(H1("7. Instructor Viva Questions & Answers (Tayari K Liye)"))
story.append(P("Agar teacher aap se viva mein sawal poochen to unhe bohot confident aur simple tareeqe se ye explain karein:"))

viva_qa = [
    ("Q1: Aap ne is project mein kaun si problem solve ki?", 
     "Sir, hum ne Dry Beans (khushk lobia) ki 7 varieties ko computer vision k 16 geometric features k zariye classify karne ka Multi-Class Classification model train kiya hai."),
    
    ("Q2: Kaun sa model sab se behtar raha aur kyun?", 
     "Sir, Support Vector Machine (SVM with RBF kernel) sab se best raha jis ki Test Accuracy 92.56% aur Macro-F1 score 0.9360 aya. Is ki waja ye hai k lobia k shape features continuous aur geometric curves par mushtamil hain, jin k liye RBF kernel boundary bohot smooth aur accurate banata hai."),
    
    ("Q3: Primary metric Accuracy kyun nahi rakhi, Macro-F1 kyun rakhi?", 
     "Sir, kyunki dataset mein class imbalance tha. Dermason k 3,546 samples the jabke Bombay k sirf 522 samples the (6.8 times farq). Agar model bari class ko zyada favor kare to accuracy high aa sakti hai lekin choti class fail ho sakti hai. Macro-F1 har class ko barabar wazan (equal weight) deta hai, is liye ye sab se fair metric hai."),
    
    ("Q4: Data Leakage se bachne k liye aap ne kya kiya?", 
     "Sir, hum ne StandardScaler ko sirf Training set (70%) par fit kiya. Validation aur Test set par sirf transform kiya. Is tarah testing data ki information training phase mein leak nahi hui."),
    
    ("Q5: Sab se zyada ghalati model kis variety mein kar raha hai?", 
     "Sir, Dermason aur Sira aapas mein sab se zyada misclassify ho rahi hain (38 Sira ko Dermason aur 33 Dermason ko Sira banaya). Dono medium-sized elliptical beans hain aur in k area, perimeter aur aspect ratio bohot zyada overlap karte hain."),
    
    ("Q6: Bombay variety ko model ne itni aasani se 100% kaise pehchan liya?", 
     "Sir, Bombay variety ka average area 170,000 pixels se bara hai, jabke baqi sab beans ka area 30,000 se 80,000 tak hai. Bombay size mein baqi sab se 4 guna bari hai, is liye feature space mein bilkul alag cluster banati hai."),
    
    ("Q7: Class weighting lagane ka kya asar hua?", 
     "Sir, class_weight='balanced' lagane se minority class par ghalati karne par model ko zyada penalty mili, jis se validation Macro-F1 0.9397 se barh kar 0.9409 ho gaya baghair overall accuracy kam kiye."),
    
    ("Q8: PCA lagane se kya faida hua?", 
     "Sir, PCA se hum ne dekha k 16 features mein bohot correlation thi (jaise Area aur ConvexArea 0.99 correlated hain). Sirf 8 components use kar k bhi hamara model 100% original Macro-F1 (0.9360) hasil kar leta hai, jis se 50% memory aur training time save hota hai."),
    
    ("Q9: Neural Network (MLP) ka result kaisa raha?", 
     "Sir, MLP ne 92.21% accuracy di jo k SVM k bohot qareeb thi (2nd best model bana). Is se pata chalta hai k deep architecture bhi is data par acha generalize kar raha hai."),
    
    ("Q10: Real life mein is project ka kya faida hai?", 
     "Sir, automated seed sorting machines mein jab conveyor belt par lobia k danay guzarte hain to high-speed camera tasweer leta hai, hamara model real-time mein variety classify karta hai aur pneumatic air nozzles k zariye har variety ko alag alag bin mein daal deta hai.")
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
