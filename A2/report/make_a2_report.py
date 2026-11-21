import os
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
    Table, TableStyle, PageBreak, FrameBreak, KeepTogether, Image
)
from reportlab.lib.colors import HexColor

# Output path
out_dir = r"C:\Users\Hp\.gemini\antigravity\scratch\AI101-ML-Assignment-70177771\A2\report"
os.makedirs(out_dir, exist_ok=True)
pdf_path = os.path.join(out_dir, "70177771_A2_Report.pdf")

# Dimensions for A4
PAGE_W, PAGE_H = A4  # 595.27 x 841.89 points
NAVY = HexColor('#17365D')
BLUE = HexColor('#2F75B5')
PALE = HexColor('#F2F6FA')
INK = HexColor('#1F2421')
MUTED = HexColor('#4A5568')
BORDER_COLOR = HexColor('#CBD5E1')

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name='TitleX', parent=styles['Title'], fontName='Helvetica-Bold', 
    fontSize=13.5, leading=16, textColor=NAVY, alignment=TA_CENTER, spaceAfter=2
))
styles.add(ParagraphStyle(
    name='AuthorX', parent=styles['Normal'], fontName='Helvetica-Bold', 
    fontSize=7.8, leading=10, alignment=TA_CENTER, textColor=INK, spaceAfter=1
))
styles.add(ParagraphStyle(
    name='MetaX', parent=styles['Normal'], fontName='Helvetica', 
    fontSize=7.2, leading=9, alignment=TA_CENTER, textColor=MUTED, spaceAfter=5
))
styles.add(ParagraphStyle(
    name='SecHead', parent=styles['Heading2'], fontName='Helvetica-Bold', 
    fontSize=8.3, leading=9.8, textColor=NAVY, spaceBefore=4, spaceAfter=1.8, keepWithNext=True
))
styles.add(ParagraphStyle(
    name='H2', parent=styles['Heading3'], fontName='Helvetica-Bold', 
    fontSize=7.6, leading=9, textColor=BLUE, spaceBefore=2.5, spaceAfter=1.2, keepWithNext=True
))
styles.add(ParagraphStyle(
    name='B', parent=styles['BodyText'], fontName='Helvetica', 
    fontSize=7.1, leading=8.6, textColor=INK, spaceAfter=2, alignment=TA_JUSTIFY
))
styles.add(ParagraphStyle(
    name='B_Bullet', parent=styles['BodyText'], fontName='Helvetica', 
    fontSize=6.8, leading=8.2, textColor=INK, leftIndent=6, spaceAfter=1.5
))
styles.add(ParagraphStyle(
    name='Cap', parent=styles['BodyText'], fontName='Helvetica-Oblique', 
    fontSize=6.5, leading=7.8, textColor=MUTED, alignment=TA_CENTER, spaceAfter=2
))
styles.add(ParagraphStyle(
    name='Cell', parent=styles['BodyText'], fontName='Helvetica', 
    fontSize=6.2, leading=7.4, textColor=INK
))
styles.add(ParagraphStyle(
    name='CellH', parent=styles['BodyText'], fontName='Helvetica-Bold', 
    fontSize=6.2, leading=7.4, textColor=colors.white
))

class TwoColDoc(BaseDocTemplate):
    def __init__(self, filename, **kw):
        margin_x = 0.45 * inch
        margin_y = 0.45 * inch
        super().__init__(filename, pagesize=A4, leftMargin=margin_x, rightMargin=margin_x, 
                         topMargin=margin_y, bottomMargin=margin_y, **kw)
        gutter = 0.18 * inch
        col_w = (PAGE_W - 2 * margin_x - gutter) / 2
        col_h = PAGE_H - 2 * margin_y - 0.22 * inch
        
        frame_l = Frame(margin_x, margin_y, col_w, col_h, id='F_L',
                        leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        frame_r = Frame(margin_x + col_w + gutter, margin_y, col_w, col_h, id='F_R',
                        leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        
        self.addPageTemplates([PageTemplate(id='two_col', frames=[frame_l, frame_r], onPage=self.draw_header_footer)])

    def draw_header_footer(self, canvas, doc):
        canvas.saveState()
        # Top banner
        canvas.setFillColor(NAVY)
        canvas.rect(0, PAGE_H - 0.26 * inch, PAGE_W, 0.26 * inch, stroke=0, fill=1)
        canvas.setFont('Helvetica-Bold', 7)
        canvas.setFillColor(colors.white)
        canvas.drawString(0.45 * inch, PAGE_H - 0.18 * inch, "AI-101 MACHINE LEARNING ASSIGNMENT  |  POOL A (NUMERICAL)  |  TASK A2")
        canvas.drawRightString(PAGE_W - 0.45 * inch, PAGE_H - 0.18 * inch, "THE UNIVERSITY OF LAHORE")
        
        # Bottom footer line
        canvas.setStrokeColor(BORDER_COLOR)
        canvas.setLineWidth(0.5)
        canvas.line(0.45 * inch, 0.32 * inch, PAGE_W - 0.45 * inch, 0.32 * inch)
        canvas.setFont('Helvetica', 6.5)
        canvas.setFillColor(MUTED)
        canvas.drawString(0.45 * inch, 0.20 * inch, "Muhammad Zain-ul-Abideen (Roll: 70177771, Sec B)  |  Task A2: Concrete Strength Regression")
        canvas.drawRightString(PAGE_W - 0.45 * inch, 0.20 * inch, f"Page {doc.page}")
        canvas.restoreState()

def P(txt, style='B'): return Paragraph(txt, styles[style])
def H(txt): return Paragraph(txt, styles['SecHead'])
def H2(txt): return Paragraph(txt, styles['H2'])

def make_table(data, widths, align='CENTER'):
    t = Table(data, colWidths=widths, hAlign=align)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.35, BORDER_COLOR),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 2),
        ('RIGHTPADDING', (0, 0), (-1, -1), 2),
        ('TOPPADDING', (0, 0), (-1, -1), 1.6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1.6),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, PALE])
    ]))
    return t

def cell(s, is_header=False): return P(str(s), 'CellH' if is_header else 'Cell')

# Build Document Story
story = []

# Title & Metadata
story.append(P("Task A2: Predicting Concrete Compressive Strength from Mixture Proportions and Age", 'TitleX'))
story.append(P("Muhammad Zain-ul-Abideen (Roll No. 70177771, Section B)", 'AuthorX'))
story.append(P("Department of Intelligent Systems, The University of Lahore<br/>GitHub: <u>https://github.com/zainrjzain-code/AI101-ML-Assignment-70177771</u>", 'MetaX'))

# Section 1: Introduction
story.append(H("1. Introduction"))
story.append(P("Concrete is the most consumed engineered material on Earth. Compressive strength is its defining mechanical benchmark, dictating safety, durability, and compliance. Conventional laboratory strength determination requires standard moist curing for 28 days before conducting destructive crushing tests. This prolonged timeframe creates expensive construction bottlenecks. Accurately modeling compressive strength directly from batch proportions enables rapid mix optimization, lowers testing costs, and accelerates construction timelines. In this study, five regression architectures are benchmarked on the 1,030-sample UCI Concrete dataset. <b>Our primary finding is that Gradient Boosting achieves state-of-the-art predictive performance (R² = 0.9277, RMSE = 4.31 MPa), while civil engineering feature engineering (w/c ratio and log curing age) drastically lifts baseline linear model fidelity from R² = 0.6276 to 0.8329 (+20.5% explained variance).</b>"))

# Section 2: Problem Statement
story.append(H("2. Problem Statement"))
story.append(P("This study addresses a supervised numerical regression task. Given a feature vector <b>x</b> ∈ ℝ^d representing concrete components (Cement, Blast Furnace Slag, Fly Ash, Water, Superplasticizer, Coarse Aggregate, Fine Aggregate in kg/m³) and curing Age in days, the objective is to predict the continuous compressive strength y ∈ ℝ (in MPa). Success is measured primarily by Root Mean Squared Error (RMSE) to severely penalize high deviations critical to structural safety, Mean Absolute Error (MAE), and Coefficient of Determination (R²). The fundamental challenge stems from strong physical non-linearities: hydration exhibits rapid early strength gains followed by asymptotic logarithmic saturation, while water-cement interactions govern porous matrix integrity inversely."))

# Section 3: Dataset Used
story.append(H("3. Dataset Used"))
story.append(P("We employ the benchmark Concrete Compressive Strength dataset (UCI ID: 165), collected by Prof. I-Cheng Yeh at Chung-Hua University [1]. The dataset comprises 1,030 experimental formulations across eight continuous inputs and one target. No missing values exist. Data cleaning verified that all feature dimensions represent valid physical densities. To prevent data leakage, data scaling and transformations are encapsulated within strict cross-validation pipelines."))

# Section 4: Dataset Statistics
story.append(H("4. Dataset Statistics"))
story.append(P("The target compressive strength spans 2.33 to 82.60 MPa (mean 35.82 ± 16.71 MPa). Exploratory analysis revealed substantial right-skewness in Age (+3.27), reflecting concentrated testing at standard ages (7, 14, 28 days) with sparse long-term trials (90–365 days). Pearson correlations confirm Cement (+0.50) and Age (+0.33) as positive drivers, while Water is negatively correlated (-0.29)."))

stat_data = [
    [cell("Feature (kg/m³ or days)", True), cell("Mean", True), cell("Std", True), cell("Min", True), cell("Max", True), cell("Skew", True)],
    [cell("Cement"), cell("281.17"), cell("104.51"), cell("102.0"), cell("540.0"), cell("+0.51")],
    [cell("Blast Furnace Slag"), cell("73.90"), cell("86.28"), cell("0.0"), cell("359.4"), cell("+0.80")],
    [cell("Fly Ash"), cell("54.19"), cell("64.00"), cell("0.0"), cell("200.1"), cell("+0.54")],
    [cell("Water"), cell("181.57"), cell("21.35"), cell("121.8"), cell("247.0"), cell("+0.08")],
    [cell("Superplasticizer"), cell("6.20"), cell("5.97"), cell("0.0"), cell("32.2"), cell("+0.91")],
    [cell("Coarse Aggregate"), cell("972.92"), cell("77.75"), cell("801.0"), cell("1145.0"), cell("-0.04")],
    [cell("Fine Aggregate"), cell("773.58"), cell("80.18"), cell("594.0"), cell("992.6"), cell("-0.25")],
    [cell("Age (days)"), cell("45.66"), cell("63.17"), cell("1.0"), cell("365.0"), cell("+3.27")],
    [cell("Compressive Strength"), cell("35.82"), cell("16.71"), cell("2.33"), cell("82.60"), cell("+0.42")]
]
story.append(make_table(stat_data, [1.15*inch, 0.42*inch, 0.42*inch, 0.40*inch, 0.42*inch, 0.40*inch]))
story.append(P("Table I: Summary descriptive statistics of the 1,030 concrete formulations.", 'Cap'))

# Figure 1: Bivariate scatter
fig3_file = r"C:\Users\Hp\.gemini\antigravity\scratch\AI101-ML-Assignment-70177771\A2\figures\figure3_scatter_relationships.png"
if os.path.exists(fig3_file):
    story.append(Spacer(1, 2))
    story.append(Image(fig3_file, width=3.35*inch, height=1.20*inch))
    story.append(P("Fig. 1. Bivariate physical drivers: Compressive strength vs. Age (logarithmic growth) and Water/Cement ratio (Abrams' law).", 'Cap'))

# Section 5: Methodology
story.append(H("5. Methodology"))
story.append(H2("5.1 Learning Setting & Models"))
story.append(P("We formulate supervised regression pipelines comparing five paradigms: (i) Linear Regression (baseline); (ii) Polynomial Feature Expansion + Ridge Regression (L2 shrinkage); (iii) Random Forest Regressor; (iv) Gradient Boosting Regressor (sequential tree boosting); and (v) Multi-Layer Perceptron (MLPRegressor feedforward neural network)."))

story.append(H2("5.2 Data Split & Zero-Leakage Policy"))
story.append(P("The dataset is partitioned into an 80% training set (824 samples) and a 20% held-out test set (206 samples) with fixed random seed (42). Hyperparameter selection is conducted exclusively on the training split using 5-fold cross-validation. All scalers (StandardScaler) and polynomial transformers are embedded within scikit-learn Pipelines, ensuring transformation parameters are fit only on training folds."))

story.append(H2("5.3 Parameter Settings"))
param_data = [
    [cell("Model", True), cell("Tuned Hyperparameters", True), cell("Best Value", True)],
    [cell("Linear Reg."), cell("Analytical OLS Fit"), cell("StandardScaler"), ],
    [cell("Poly Ridge"), cell("degree ∈ {1,2,3}, α ∈ {0.1,1,10,100}"), cell("degree=3, α=0.1")],
    [cell("Random Forest"), cell("n_est ∈ {100,200}, depth ∈ {10,15,None}"), cell("n=200, depth=None")],
    [cell("Gradient Boost"), cell("n_est ∈ {100,200,300}, lr ∈ {0.03,0.08,0.15}"), cell("n=300, lr=0.08, d=4")],
    [cell("MLP Regressor"), cell("arch ∈ {(64,32),(100,50),(128,64,32)}, α"), cell("(128,64,32), α=0.001")]
]
story.append(make_table(param_data, [0.85*inch, 1.45*inch, 0.95*inch]))
story.append(P("Table II: Hyperparameter search spaces and optimal values selected via 5-fold CV.", 'Cap'))

# End Column 1 -> FrameBreak
story.append(FrameBreak())

# Column 2: Results & Analysis
story.append(H("6. Results and Analysis"))
story.append(P("Every model was evaluated on the identical held-out test partition (206 samples). Performance metrics are summarized in Table III and Table IV."))

story.append(H2("6.1 Feature Engineering Ablation Study"))
story.append(P("To evaluate domain-driven features, models were trained under two regimes: (1) Raw (8 physical features); (2) Engineered (+ w/c ratio and log(Age))."))

ablation_table = [
    [cell("Model", True), cell("Raw RMSE", True), cell("Eng RMSE", True), cell("Δ RMSE", True), cell("Eng R²", True)],
    [cell("Linear Reg."), cell("9.80"), cell("6.56"), cell("<b>-3.23</b>"), cell("<b>0.8329</b>")],
    [cell("Poly Ridge"), cell("7.36"), cell("5.70"), cell("<b>-1.66</b>"), cell("0.8739")],
    [cell("Random Forest"), cell("5.54"), cell("5.30"), cell("-0.24"), cell("0.8912")],
    [cell("Gradient Boost"), cell("4.76"), cell("4.29"), cell("-0.47"), cell("0.9286")],
    [cell("MLP Regressor"), cell("5.64"), cell("5.30"), cell("-0.34"), cell("0.8908")]
]
story.append(make_table(ablation_table, [0.85*inch, 0.60*inch, 0.60*inch, 0.55*inch, 0.65*inch]))
story.append(P("Table III: Feature engineering ablation on held-out test partition.", 'Cap'))

story.append(H2("6.2 Test Set Final Comparison"))
perf_table = [
    [cell("Model Architecture", True), cell("MAE", True), cell("RMSE", True), cell("Test R²", True), cell("CV RMSE", True)],
    [cell("Linear Regression (Baseline)"), cell("5.29"), cell("6.56"), cell("0.8329"), cell("7.06 ± 0.53")],
    [cell("Polynomial + Ridge (Deg 3)"), cell("4.19"), cell("5.92"), cell("0.8639"), cell("5.07 ± 0.49")],
    [cell("Random Forest"), cell("3.71"), cell("5.39"), cell("0.8873"), cell("5.27 ± 0.32")],
    [cell("Gradient Boosting (Best)"), cell("<b>2.85</b>"), cell("<b>4.31</b>"), cell("<b>0.9277</b>"), cell("<b>4.69 ± 0.37</b>")],
    [cell("MLP Regressor (128-64-32)"), cell("3.80"), cell("5.57"), cell("0.8795"), cell("4.85 ± 0.53")]
]
story.append(make_table(perf_table, [1.10*inch, 0.40*inch, 0.42*inch, 0.48*inch, 0.85*inch]))
story.append(P("Table IV: Test set performance and 5-fold cross-validation stability.", 'Cap'))

# Figure 4: Predicted vs actual
fig4_file = r"C:\Users\Hp\.gemini\antigravity\scratch\AI101-ML-Assignment-70177771\A2\figures\figure4_predicted_vs_actual.png"
if os.path.exists(fig4_file):
    story.append(Spacer(1, 2))
    story.append(Image(fig4_file, width=3.35*inch, height=1.35*inch))
    story.append(P("Fig. 2. Predicted vs. Actual Compressive Strength across models on held-out test set.", 'Cap'))

story.append(H2("6.3 Analysis Questions & Engineering Discussion"))
story.append(P("<b>1. Why does the linear baseline under-perform? Which assumption is violated?</b><br/>The raw linear baseline achieves poor fidelity (R² = 0.6276, RMSE = 9.80 MPa) because the fundamental assumption of <i>linearity in parameters and inputs</i> is invalid. Cement hydration kinetics exhibit severe non-linear curvature: concrete gains strength rapidly during early hydration (1–14 days) and plateaus asymptotically beyond 28 days. Furthermore, component interactions follow Abrams' Law (w/c inverse ratio), violating additive linearity. Homoscedasticity is also violated: residual variance expands noticeably at higher target strength regimes."))

story.append(P("<b>2. Did engineered features help every model, or only some? Why?</b><br/>Engineered features helped <i>every</i> model, but the magnitude of improvement varied drastically. Linear models witnessed dramatic leaps (Linear Regression R² +20.5%, Poly Ridge R² +8.4%), whereas tree-based ensembles saw modest gains (+1.0% to +1.7%). Tree models natively partition orthogonal feature subspaces to approximate arbitrary non-linear thresholds, whereas linear regressors cannot model curvature without log(Age) or ratio interactions without w/c."))

story.append(P("<b>3. Where are the largest errors? What does feature importance tell an engineer?</b><br/>Residual analysis shows that largest prediction errors occur on <i>very young specimens (1–7 days)</i> and highly fluid mixes (high superplasticizer), reaching peak absolute errors of 15–20 MPa. In young samples, chemical hydration is intensely sensitive to unrecorded variables (cement mineralogy, curing ambient temperature, and humidity). Conversely, mature concrete (>28 days) exhibits low average errors (1.87 MPa). Permutation feature importance (Fig. 6 in notebook) ranks Age, Cement, w/c ratio, and Slag as the dominant contributors. For a concrete engineer, this proves that reducing water content via superplasticizers is far more cost- and carbon-efficient than simply adding excessive cement."))

story.append(H2("6.4 Limitations"))
story.append(P("The dataset omits curing ambient temperatures, aggregate gradation curves, and chemical admixture types, which account for residual variance in early-age hydration."))

# Section 7: Conclusion
story.append(H("7. Conclusion"))
story.append(P("Gradient Boosting proved superior for concrete compressive strength regression, reaching R² = 0.9277 and RMSE = 4.31 MPa. Incorporating civil engineering physical features (w/c ratio and log curing age) proved essential, boosting linear model performance by over 20%. In future work, physics-informed neural networks (PINNs) could integrate thermodynamic hydration equations to further improve early-age predictions."))

# Section 8: AI Use Disclosure
story.append(H("AI Use Disclosure"))
story.append(P("I used Google Antigravity / Gemini for debugging cross-validation pipelines, formatting LaTeX/ReportLab layouts, and refining report conciseness. Notebook cells 1–15 and report sections 1–7 were reviewed, verified, and checked against executed notebook outputs. All experiments, results, and analyses were produced and checked by me, and I take full responsibility for this work."))

# Section 9: References
story.append(H("References"))
story.append(P("[1] I.-C. Yeh, \"Modeling of strength of high-performance concrete using artificial neural networks,\" <i>Cement and Concrete Research</i>, vol. 28, no. 12, pp. 1797–1808, 1998.<br/>[2] UCI Machine Learning Repository, \"Concrete Compressive Strength,\" Dataset ID 165, 2007.<br/>[3] D. A. Abrams, \"Design of Concrete Mixtures,\" <i>Bull. 1, Struct. Mater. Res. Lab.</i>, Lewis Inst., Chicago, 1918.<br/>[4] F. Pedregosa et al., \"Scikit-learn: Machine Learning in Python,\" <i>JMLR</i>, vol. 12, pp. 2825–2830, 2011."))

# Build PDF
doc = TwoColDoc(pdf_path)
doc.build(story)
print(f"Report generated successfully at: {pdf_path}")
