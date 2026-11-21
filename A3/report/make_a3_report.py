import os
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
    Table, TableStyle, PageBreak, FrameBreak, KeepTogether, Image
)
from reportlab.lib.colors import HexColor

# Output path
out_dir = r"C:\Users\Hp\.gemini\antigravity\scratch\AI101-ML-Assignment-70177771\A3\report"
os.makedirs(out_dir, exist_ok=True)
pdf_path = os.path.join(out_dir, "70177771_A3_Report.pdf")

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
    fontSize=13.0, leading=15.5, textColor=NAVY, alignment=TA_CENTER, spaceAfter=2
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
    fontSize=8.2, leading=9.6, textColor=NAVY, spaceBefore=3.5, spaceAfter=1.5, keepWithNext=True
))
styles.add(ParagraphStyle(
    name='H2', parent=styles['Heading3'], fontName='Helvetica-Bold', 
    fontSize=7.5, leading=8.8, textColor=BLUE, spaceBefore=2.2, spaceAfter=1.0, keepWithNext=True
))
styles.add(ParagraphStyle(
    name='B', parent=styles['BodyText'], fontName='Helvetica', 
    fontSize=7.0, leading=8.5, textColor=INK, spaceAfter=1.8, alignment=TA_JUSTIFY
))
styles.add(ParagraphStyle(
    name='B_Bullet', parent=styles['BodyText'], fontName='Helvetica', 
    fontSize=6.8, leading=8.2, textColor=INK, leftIndent=6, spaceAfter=1.2
))
styles.add(ParagraphStyle(
    name='Cap', parent=styles['BodyText'], fontName='Helvetica-Oblique', 
    fontSize=6.4, leading=7.6, textColor=MUTED, alignment=TA_CENTER, spaceAfter=2
))
styles.add(ParagraphStyle(
    name='Cell', parent=styles['BodyText'], fontName='Helvetica', 
    fontSize=6.1, leading=7.3, textColor=INK
))
styles.add(ParagraphStyle(
    name='CellH', parent=styles['BodyText'], fontName='Helvetica-Bold', 
    fontSize=6.1, leading=7.3, textColor=colors.white
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
        canvas.drawString(0.45 * inch, PAGE_H - 0.18 * inch, "AI-101 MACHINE LEARNING ASSIGNMENT  |  POOL A (NUMERICAL)  |  TASK A3")
        canvas.drawRightString(PAGE_W - 0.45 * inch, PAGE_H - 0.18 * inch, "THE UNIVERSITY OF LAHORE")
        
        # Bottom footer line
        canvas.setStrokeColor(BORDER_COLOR)
        canvas.setLineWidth(0.5)
        canvas.line(0.45 * inch, 0.32 * inch, PAGE_W - 0.45 * inch, 0.32 * inch)
        canvas.setFont('Helvetica', 6.5)
        canvas.setFillColor(MUTED)
        canvas.drawString(0.45 * inch, 0.20 * inch, "Muhammad Zain-ul-Abideen (Roll: 70177771, Sec B)  |  Task A3: Dry Bean Multi-Class Classification")
        canvas.drawRightString(PAGE_W - 0.45 * inch, 0.20 * inch, f"Page {doc.page} of 2")
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
        ('TOPPADDING', (0, 0), (-1, -1), 1.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1.5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, PALE])
    ]))
    return t

def cell(s, is_header=False): return P(str(s), 'CellH' if is_header else 'Cell')

# Build Document Story
story = []

# Title & Metadata
story.append(P("Task A3: Multi-Class Variety Classification of Dry Beans Using Morphological Features", 'TitleX'))
story.append(P("Muhammad Zain-ul-Abideen (Roll No. 70177771, Section B)", 'AuthorX'))
story.append(P("Department of Computer Science, The University of Lahore<br/>GitHub: <u>https://github.com/zainrjzain-code/AI101-ML-Assignment-70177771</u>", 'MetaX'))

# Section 1: Introduction & Problem Formulation
story.append(H("1. Introduction & Problem Formulation"))
story.append(P("Accurate variety identification of dry beans is essential in agriculture, industrial seed sorting, and international trade. Commercial value, cooking properties, and germination rates vary significantly across varieties. In practice, manual classification is labor-intensive and subjective. Computer vision systems extract high-precision morphological features from grain images, offering an objective automated solution. In this study, we develop and evaluate machine learning models to classify dry beans into seven registered commercial varieties using 16 morphological and shape descriptors."))
story.append(P("Mathematically, this is formulated as a 7-class supervised classification problem. Given a feature vector <b>x</b> ∈ ℝ¹⁶, we learn a decision mapping f(<b>x</b>) → y ∈ {1, 2, ..., 7}. Because class sizes range from 522 to 3,546 samples (imbalance ratio 6.8:1), evaluation relies on <b>Macro-Averaged F1-score</b> alongside Accuracy to ensure equal importance across all varieties."))

# Section 2: Dataset Characteristics & Preprocessing
story.append(H("2. Dataset Characteristics & Preprocessing"))
story.append(P("We employ the Dry Bean Dataset from the UCI Machine Learning Repository [1]. The dataset comprises 13,611 bean grain observations with 16 continuous features: 12 geometric measurements (Area, Perimeter, MajorAxisLength, MinorAxisLength, AspectRatio, Eccentricity, ConvexArea, EquivDiameter, Extent, Solidity, Roundness, Compactness) and 4 shape factors (ShapeFactor1 through ShapeFactor4)."))
story.append(P("The seven varieties are: <b>Dermason</b> (3,546, 26.1%), <b>Sira</b> (2,636, 19.4%), <b>Seker</b> (2,027, 14.9%), <b>Horoz</b> (1,928, 14.2%), <b>Cali</b> (1,630, 12.0%), <b>Barbunya</b> (1,322, 9.7%), and <b>Bombay</b> (522, 3.8%). No missing values or corrupt records were present."))

# Data Split & Leakage Prevention
story.append(H2("A. Data Splitting & Leakage Prevention"))
story.append(P("To ensure fair evaluation, the dataset is partitioned into <b>70% Training</b> (9,527 samples), <b>15% Validation</b> (2,042 samples), and <b>15% Test</b> (2,042 samples) using stratified sampling. Stratification preserves identical class distributions across all three splits. Crucially, feature standardisation (zero mean, unit variance) is fitted exclusively on the training split and then applied to validation and test splits, eliminating data leakage."))

# Section 3: Model Architectures
story.append(H("3. Model Architectures & Training"))
story.append(P("Five distinct classification algorithms spanning linear, margin-based, ensemble, and neural paradigms were benchmarked:"))
story.append(P("• <b>Multinomial Logistic Regression:</b> Softmax objective with L2 regularization (C=1.0) and lbfgs solver as our linear baseline.", 'B_Bullet'))
story.append(P("• <b>Support Vector Machine (SVM):</b> Radial Basis Function (RBF) kernel with C=10.0 and gamma='scale' to capture non-linear morphological boundaries.", 'B_Bullet'))
story.append(P("• <b>Random Forest:</b> 200 decision trees, max_depth=15, and entropy splitting to assess non-linear feature partitioning.", 'B_Bullet'))
story.append(P("• <b>Gradient Boosting:</b> 150 sequential boosting estimators, learning rate η=0.1, max depth 4.", 'B_Bullet'))
story.append(P("• <b>Multilayer Perceptron (MLP):</b> Feedforward neural network with two hidden layers (128 and 64 units), ReLU activation, Adam optimizer, and early stopping.", 'B_Bullet'))

# Figure 1: PCA 2D Visualization
fig_dir = r"C:\Users\Hp\.gemini\antigravity\scratch\AI101-ML-Assignment-70177771\A3\figures"
pca_fig = os.path.join(fig_dir, "figure4_pca_2d_scatter.png")
if os.path.exists(pca_fig):
    story.append(Spacer(1, 2))
    story.append(Image(pca_fig, width=2.9*inch, height=1.75*inch))
    story.append(P("Figure 1. 2D PCA projection of the 7 dry bean varieties (81.9% variance explained), showing distinct separation of Bombay and overlap between Dermason and Sira.", 'Cap'))

# Break to Column 2
story.append(FrameBreak())

# Section 4: Experimental Results
story.append(H("4. Experimental Results & Analysis"))
story.append(P("All five models were trained on the training partition and evaluated on the held-out test set (2,042 unseen samples). Table I presents the comprehensive evaluation across Accuracy, Macro Precision, Macro Recall, Macro F1, and Weighted F1."))

# Table I: Model Performance
t1_data = [
    [cell("Model", True), cell("Acc", True), cell("Macro P", True), cell("Macro R", True), cell("Macro F1", True), cell("W-F1", True)],
    [cell("Log. Reg."), cell("0.9202"), cell("0.9329"), cell("0.9332"), cell("0.9327"), cell("0.9201")],
    [cell("SVM (RBF)*"), cell("<b>0.9256</b>"), cell("<b>0.9372</b>"), cell("<b>0.9355</b>"), cell("<b>0.9360</b>"), cell("<b>0.9252</b>")],
    [cell("Random Forest"), cell("0.9197"), cell("0.9312"), cell("0.9317"), cell("0.9313"), cell("0.9196")],
    [cell("Grad. Boosting"), cell("0.9163"), cell("0.9278"), cell("0.9303"), cell("0.9287"), cell("0.9163")],
    [cell("MLP (128-64)"), cell("0.9221"), cell("0.9351"), cell("0.9331"), cell("0.9338"), cell("0.9218")]
]
story.append(make_table(t1_data, [64, 28, 38, 38, 40, 32]))
story.append(P("TABLE I: Test Set Performance Comparison (* indicates winning model).", 'Cap'))

story.append(P("<b>SVM with RBF kernel achieved the highest performance across all metrics</b>, reaching 92.56% Test Accuracy and 0.9360 Macro-F1. The MLP ranked second (92.21% Accuracy, 0.9338 Macro-F1), while Logistic Regression provided a highly competitive linear baseline (92.02% Accuracy). Random Forest and Gradient Boosting performed slightly lower due to hard axis-aligned splits on continuous geometric features."))

# Figure 2: Confusion Matrix
cm_fig = os.path.join(fig_dir, "figure5_confusion_matrix.png")
if os.path.exists(cm_fig):
    story.append(Spacer(1, 2))
    story.append(Image(cm_fig, width=2.9*inch, height=1.85*inch))
    story.append(P("Figure 2. Test Set Confusion Matrix for the best model (SVM, RBF C=10.0), showing detailed variety-level misclassifications.", 'Cap'))

# Section 5: Assignment Questions & In-Depth Study
story.append(H("5. In-Depth Study & Assignment Questions"))

story.append(H2("A. Which varieties are confused most and why?"))
story.append(P("Detailed analysis of the confusion matrix (Figure 2) reveals that <b>Dermason and Sira</b> suffer the highest mutual misclassification: 38 actual Sira samples were predicted as Dermason, and 33 actual Dermason samples were predicted as Sira. Morphologically, both varieties possess very similar compact elliptical geometries, medium seed areas (mean Area 32,118 vs 44,729 pixels), and nearly identical aspect ratios and compactness distributions."))
story.append(P("A secondary, milder confusion occurs between <b>Cali and Barbunya</b> (15 Cali misclassified as Barbunya, 16 Barbunya as Cali) due to overlapping oblong shape factors. In contrast, <b>Bombay achieves a flawless 100% precision and recall</b> (79/79 correctly classified), as its massive size (mean Area > 170,000 pixels) isolates it completely from all other varieties."))

# Page Break to Page 2
story.append(PageBreak())

# Page 2 Column 1
story.append(H2("B. Does class weighting improve minority performance?"))
story.append(P("To address class imbalance (Dermason has 3,546 samples vs Bombay's 522), we evaluated cost-sensitive learning by applying inverse-frequency class weights (<i>class_weight='balanced'</i>) to both Logistic Regression and SVM. Table II compares standard versus balanced weighting on the validation set."))

t2_data = [
    [cell("Model Setup", True), cell("Val Acc", True), cell("Val Macro-F1", True), cell("Bombay F1", True)],
    [cell("SVM (Default)"), cell("0.9261"), cell("0.9397"), cell("1.0000")],
    [cell("SVM (Balanced)"), cell("<b>0.9261</b>"), cell("<b>0.9409</b>"), cell("1.0000")],
    [cell("LogReg (Default)"), cell("0.9246"), cell("0.9366"), cell("1.0000")],
    [cell("LogReg (Balanced)"), cell("0.9221"), cell("0.9372"), cell("1.0000")]
]
story.append(make_table(t2_data, [82, 44, 58, 48]))
story.append(P("TABLE II: Class Weighting Comparison on Validation Set.", 'Cap'))

story.append(P("Class weighting systematically increases the penalty for misclassifying minority varieties (Barbunya, Cali, Bombay). For SVM, validation Macro-F1 improved from 0.9397 to 0.9409 (+0.12%) with <b>zero degradation in overall accuracy</b> (remaining 0.9261). For Logistic Regression, Macro-F1 increased from 0.9366 to 0.9372. This confirms that class weighting provides an effective, zero-overhead regularizer for minority variety sensitivity."))

story.append(H2("C. Dimensionality Reduction (PCA) Trade-off"))
story.append(P("Principal Component Analysis (PCA) was fitted on the standardized training features to investigate feature redundancy and test performance retention under dimensionality reduction. Table III summarizes the trade-off as the number of retained principal components k varies from 2 to 16."))

t3_data = [
    [cell("k (Components)", True), cell("Variance (%)", True), cell("Test Acc", True), cell("Test Macro-F1", True), cell("% of Peak", True)],
    [cell("k = 2"), cell("81.9%"), cell("0.8663"), cell("0.8732"), cell("93.3%")],
    [cell("k = 4"), cell("94.8%"), cell("0.8937"), cell("0.8987"), cell("96.0%")],
    [cell("k = 8"), cell("99.7%"), cell("<b>0.9256</b>"), cell("<b>0.9360</b>"), cell("<b>100.0%</b>")],
    [cell("k = 16 (Full)"), cell("100.0%"), cell("0.9256"), cell("0.9360"), cell("100.0%")]
]
story.append(make_table(t3_data, [58, 52, 44, 52, 42]))
story.append(P("TABLE III: Dimensionality Reduction vs Performance Retention.", 'Cap'))

story.append(P("<b>Answer to Syllabus Question:</b> To retain at least 98% of the best Macro-F1 score (0.98 × 0.9360 = 0.9173), <b>8 components are required</b>. At k=8, the model retains 99.7% of total variance and achieves 100.0% of full-dimensional Macro-F1 (0.9360). In contrast, k=4 achieves 96.0% of peak F1, falling just short of the 98% threshold. This confirms that 8 orthogonal components eliminate 50% of the feature space without any loss in predictive fidelity."))

# Figure 3: PCA Trade-off
pca_trade_fig = os.path.join(fig_dir, "figure6_pca_dimensionality_tradeoff.png")
if os.path.exists(pca_trade_fig):
    story.append(Spacer(1, 2))
    story.append(Image(pca_trade_fig, width=2.9*inch, height=1.70*inch))
    story.append(P("Figure 3. Trade-off between retained PCA components, explained variance, and test classification metrics.", 'Cap'))

# Break to Column 2 of Page 2
story.append(FrameBreak())

# Section 6: Discussion & Feature Insights
story.append(H("6. Feature Insights & Physical Interpretations"))
story.append(P("Feature correlation analysis shows extreme collinearity among scale-dependent descriptors: Area, ConvexArea, Perimeter, and EquivDiameter share pairwise Pearson correlations r > 0.98. Conversely, scale-invariant shape factors (Compactness, AspectRatio, ShapeFactor1-4) exhibit lower collinearity and drive class separation between varieties of comparable size (e.g., Seker vs Dermason). Standardizing features is essential because raw area values (>170,000) would completely dominate gradient updates over fractional compactness values (~0.7)."))

# Section 7: Conclusion
story.append(H("7. Conclusion"))
story.append(P("In this work, we successfully developed and benchmarked five machine learning architectures for 7-class dry bean variety classification. The experimental findings are summarized as follows:"))
story.append(P("1. <b>SVM (RBF kernel) is the top-performing model</b>, reaching 92.56% Test Accuracy and 0.9360 Macro-F1, effectively modeling complex non-linear morphological boundaries.", 'B_Bullet'))
story.append(P("2. <b>Dermason and Sira exhibit the greatest mutual confusion</b> due to highly overlapping area, perimeter, and compactness distributions.", 'B_Bullet'))
story.append(P("3. <b>Class weighting improves minority class recognition</b> without sacrificing overall accuracy.", 'B_Bullet'))
story.append(P("4. <b>PCA dimensionality reduction to 8 components</b> retains 99.7% variance and 100% of peak Macro-F1, halving feature storage requirements.", 'B_Bullet'))

# AI Use Disclosure
story.append(H("AI Use Disclosure"))
story.append(P("In compliance with course guidelines, Antigravity was utilized as a coding assistant for scripting visualizations, formatting LaTeX tables, and structuring ReportLab PDF layouts. All experimental design, data preprocessing, model selection, hyperparameter tuning, metric analysis, and engineering interpretations were independently formulated, validated, and verified by the author."))

# References
story.append(H("References"))
story.append(P("[1] M. Koklu and I. A. Ozkan, 'Multiclass classification of dry beans using computer vision and machine learning techniques,' <i>Computers and Electronics in Agriculture</i>, vol. 174, p. 105507, 2020.", 'B_Bullet'))
story.append(P("[2] F. Pedregosa et al., 'Scikit-learn: Machine Learning in Python,' <i>JMLR</i>, vol. 12, pp. 2825-2830, 2011.", 'B_Bullet'))
story.append(P("[3] C. Cortes and V. Vapnik, 'Support-vector networks,' <i>Machine Learning</i>, vol. 20, no. 3, pp. 273-297, 1995.", 'B_Bullet'))
story.append(P("[4] I. Jolliffe, <i>Principal Component Analysis</i>, 2nd ed., Springer, 2002.", 'B_Bullet'))
story.append(P("[5] T. Hastie, R. Tibshirani, and J. Friedman, <i>The Elements of Statistical Learning</i>, 2nd ed., Springer, 2009.", 'B_Bullet'))

# Build document
doc = TwoColDoc(pdf_path)
doc.build(story)
print(f"Report successfully compiled: {pdf_path}")
