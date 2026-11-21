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
out_dir = r"C:\Users\Hp\.gemini\antigravity\scratch\AI101-ML-Assignment-70177771\B2\report"
os.makedirs(out_dir, exist_ok=True)
pdf_path = os.path.join(out_dir, "70177771_B2_Report.pdf")

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
        canvas.drawString(0.45 * inch, PAGE_H - 0.18 * inch, "AI-101 MACHINE LEARNING ASSIGNMENT  |  POOL B (MIXED MODALITY)  |  TASK B2")
        canvas.drawRightString(PAGE_W - 0.45 * inch, PAGE_H - 0.18 * inch, "THE UNIVERSITY OF LAHORE")
        
        # Bottom footer line
        canvas.setStrokeColor(BORDER_COLOR)
        canvas.setLineWidth(0.5)
        canvas.line(0.45 * inch, 0.32 * inch, PAGE_W - 0.45 * inch, 0.32 * inch)
        canvas.setFont('Helvetica', 6.5)
        canvas.setFillColor(MUTED)
        canvas.drawString(0.45 * inch, 0.20 * inch, "Muhammad Zain-ul-Abideen (Roll: 70177771, Sec B)  |  Task B2: Wine Critic Score Regression")
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
story.append(P("Task B2: Predicting Wine Critic Scores from Tasting Notes and Metadata", 'TitleX'))
story.append(P("Muhammad Zain-ul-Abideen (Roll No. 70177771, Section B)", 'AuthorX'))
story.append(P("Department of Computer Science, The University of Lahore<br/>GitHub: <u>https://github.com/zainrjzain-code/AI101-ML-Assignment-70177771</u>", 'MetaX'))

# Section 1: Introduction & Problem Formulation
story.append(H("1. Introduction & Problem Formulation"))
story.append(P("Professional wine evaluations significantly influence commercial pricing, investment cellarage, and global market reputation. Sommelier ratings, typically standardized on a 100-point scale (ranging in practice between 80 and 100), synthesize multidimensional sensory criteria including aroma, structural balance, tannin texture, and aging potential. Accurately modeling these scores directly from unstructured sensory notes and bottle metadata enables automated portfolio benchmarking and price-to-quality discovery."))
story.append(P("Mathematically, this is formulated as a <b>mixed-modality supervised regression task</b>. Given an instance containing structured attributes (price, origin, variety, taster) and unstructured natural language text (tasting description), the objective is to predict the continuous score y ∈ [80, 100]. Performance is evaluated via Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and the Coefficient of Determination (R²)."))

# Section 2: Dataset Characteristics & De-duplication
story.append(H("2. Dataset Exploration & Mandatory De-duplication"))
story.append(P("We benchmark on the Wine Enthusiast dataset [1], containing 129,971 raw tasting reviews across 14 attributes. Target points range from 80 to 100 (mean 88.44 ± 3.09 points). Bottle prices span $4 to $3,300 with an extreme right skew (median $25.00)."))

story.append(H2("A. Mandatory De-duplication Preprocessing"))
story.append(P("A critical requirement prior to data splitting is de-duplicating exact identical tasting descriptions. The raw repository contains <b>10,016 exact duplicates (7.71% of all records)</b> resulting from syndicated reviews across vintages. Retaining duplicates causes direct data leakage across training and test splits, artificially inflating R² metrics. After de-duplication, <b>119,955 unique reviews</b> remain."))

story.append(H2("B. Partitioning & Leakage Prevention"))
story.append(P("The cleaned dataset is partitioned into an <b>80% Training set</b> (95,963 reviews), a <b>10% Validation set</b> (11,996 reviews), and a <b>10% Test set</b> (11,996 reviews). Training-set median price ($25.00) is used for missing price imputation, and all text and categorical transformers are fitted exclusively on the training split."))

# Figure 1: Predicted vs Actual & Residuals
fig_dir = r"C:\Users\Hp\.gemini\antigravity\scratch\AI101-ML-Assignment-70177771\B2\figures"
pred_fig = os.path.join(fig_dir, "figure4_predicted_vs_actual_and_residuals.png")
if os.path.exists(pred_fig):
    story.append(Spacer(1, 2))
    story.append(Image(pred_fig, width=2.9*inch, height=1.70*inch))
    story.append(P("Figure 1. Predicted vs actual points and residual distribution for Ridge regression on held-out test set (R² = 0.7689).", 'Cap'))

# Break to Column 2
story.append(FrameBreak())

# Section 3: Feature Engineering Architecture
story.append(H("3. Mixed-Modality Pipeline Architecture"))
story.append(P("Feature spaces were extracted across two modalities:"))
story.append(P("• <b>Metadata Features (108 dimensions):</b> Standardized log(1 + price), word count, char count; missing price indicator; and one-hot encodings of top 20 categories for country, province, variety, winery, and taster name (rare categories grouped as 'Other').", 'B_Bullet'))
story.append(P("• <b>Text Features (15,000 dimensions):</b> TF-IDF unigram and bigram representation of cleaned tasting notes (min_df=5, English stop words removed).", 'B_Bullet'))
story.append(P("• <b>Combined Space (15,108 dimensions):</b> Sparse horizontal concatenation of metadata and text features.", 'B_Bullet'))

# Section 4: Experimental Results & Benchmark Comparison
story.append(H("4. Experimental Results & Benchmark Comparison"))
story.append(P("Models evaluated on the test set include a Mean Baseline, SGDRegressor, and Ridge Regression. Ridge regularization parameter alpha was optimized on the validation split (alpha=5.0). Table I summarizes test set evaluation."))

# Table I: Benchmark Results
t1_data = [
    [cell("Model Architecture", True), cell("Test MAE", True), cell("Test RMSE", True), cell("Test R²", True)],
    [cell("Mean Baseline"), cell("2.522"), cell("3.070"), cell("-0.0000")],
    [cell("SGDRegressor (Squared)"), cell("1.255"), cell("1.596"), cell("0.7300")],
    [cell("Ridge Regression (α=5.0)*"), cell("<b>1.164</b>"), cell("<b>1.476</b>"), cell("<b>0.7689</b>")]
]
story.append(make_table(t1_data, [100, 48, 50, 50]))
story.append(P("TABLE I: Test Set Benchmark Performance Comparison (* indicates winning model).", 'Cap'))

story.append(P("<b>Ridge regression achieved the highest predictive performance</b>, reaching <b>R² = 0.7689 (76.89% explained variance)</b>, MAE = 1.164 points, and RMSE = 1.476 points. This outperforms the mean baseline by 53.8% error reduction."))

# Figure 2: Top Words Pushing Scores Up and Down
words_fig = os.path.join(fig_dir, "figure5_ridge_top_words_coefficients.png")
if os.path.exists(words_fig):
    story.append(Spacer(1, 2))
    story.append(Image(words_fig, width=2.9*inch, height=1.75*inch))
    story.append(P("Figure 2. Top Ridge regression coefficients: sensory descriptors pushing predicted ratings up versus down.", 'Cap'))

# Page Break to Page 2
story.append(PageBreak())

# Page 2 Column 1
# Section 5: Mandatory Modality Ablation Study
story.append(H("5. Mandatory Modality Ablation Study"))
story.append(P("To measure the incremental value of natural language tasting notes over pricing and origin metadata, Ridge regression was trained on: (i) Metadata only, (ii) Text only, and (iii) Combined. Table II presents the results."))

t2_data = [
    [cell("Modality Configuration", True), cell("Test MAE", True), cell("Test RMSE", True), cell("Test R²", True), cell("R² Gain", True)],
    [cell("Metadata Only"), cell("1.572"), cell("1.990"), cell("0.5800"), cell("Baseline")],
    [cell("Text Only (Tasting Note)"), cell("1.351"), cell("1.715"), cell("0.6879"), cell("+10.79%")],
    [cell("Combined (Metadata + Text)"), cell("<b>1.164</b>"), cell("<b>1.476</b>"), cell("<b>0.7689</b>"), cell("<b>+18.89%</b>")]
]
story.append(make_table(t2_data, [96, 38, 38, 38, 38]))
story.append(P("TABLE II: Mandatory Modality Ablation Comparison on Test Set.", 'Cap'))

story.append(P("<b>Impact of Tasting Notes:</b> Metadata alone explains 58.0% of score variance, confirming that price and pedigree strongly anchor critic ratings. However, integrating natural language tasting notes raises explained variance to <b>76.89% (+18.89% absolute gain)</b> and reduces MAE from 1.572 to 1.164 points. Sommelier vocabulary captures structural balance and sensory flaws that price metadata cannot encode."))

# Section 6: Performance per Points Band & Regression to Mean
story.append(H("6. Performance per Points Band & Regression to Mean"))
story.append(P("To evaluate performance across rating tiers, MAE was computed across four score intervals on the held-out test set (Table III)."))

t3_data = [
    [cell("Critic Points Band", True), cell("Test Samples", True), cell("Test %", True), cell("MAE (Points)", True)],
    [cell("80–84 (Lower Tier)"), cell("1,164"), cell("9.7%"), cell("1.441")],
    [cell("85–89 (Median Band)"), cell("6,283"), cell("52.4%"), cell("<b>1.027</b>")],
    [cell("90–94 (Excellent Tier)"), cell("4,301"), cell("35.9%"), cell("1.239")],
    [cell("95–100 (Classic Tier)"), cell("248"), cell("2.1%"), cell("2.048")]
]
story.append(make_table(t3_data, [88, 52, 46, 62]))
story.append(P("TABLE III: MAE by Points Band on Held-out Test Set.", 'Cap'))

# Figure 3: MAE by Band and Ablation
band_fig = os.path.join(fig_dir, "figure6_mae_by_points_band_and_ablation.png")
if os.path.exists(band_fig):
    story.append(Spacer(1, 2))
    story.append(Image(band_fig, width=2.9*inch, height=1.75*inch))
    story.append(P("Figure 3. Error per rating band demonstrating regression to the mean (left) and modality ablation summary (right).", 'Cap'))

# Break to Column 2 of Page 2
story.append(FrameBreak())

# Section 7: Assignment Specific Questions & In-Depth Discussion
story.append(H("7. Assignment Questions & In-Depth Discussion"))

story.append(H2("A. How much does the tasting note add beyond price and origin?"))
story.append(P("Tasting notes add an extraordinary <b>+18.89% explained variance (R² increases from 0.5800 to 0.7689)</b> and lower test MAE by 0.408 points per bottle. While price establishes a foundational quality tier (r = +0.61 with log price), sensory descriptions distinguish whether a premium $80 bottle represents a transcendent classic (96 points) or an over-extracted disappointment (88 points)."))

story.append(H2("B. Which words push predicted scores up or down?"))
story.append(P("Ridge regression coefficient inspection (Figure 2) reveals distinct lexical markers:"))
story.append(P("• <b>Positive Descriptors (Pushing Scores UP):</b> <i>layered</i>, <i>seamless</i>, <i>cellar</i>, <i>long finish</i>, <i>opulent</i>, <i>velvety</i>, <i>complex</i>, and <i>magnificent</i>. These terms describe depth, textural refinement, and cellaring longevity.", 'B_Bullet'))
story.append(P("• <b>Negative Descriptors (Pushing Scores DOWN):</b> <i>simple</i>, <i>sour</i>, <i>green</i>, <i>dilute</i>, <i>unripe</i>, <i>thin</i>, <i>harsh</i>, and <i>watery</i>. These terms signal underripe harvest, hollow mid-palates, and harsh unbalanced acidity.", 'B_Bullet'))

story.append(H2("C. Why are the extremes (80–82 and 95+) predicted worst?"))
story.append(P("As shown in Table III, the central tier (85–89 points) achieves the lowest error (MAE = 1.027), while the classic tier (95–100) suffers the highest error (MAE = 2.048). This is governed by <b>statistical regression to the mean and L2 regularization shrinkage</b>. Because ratings cluster heavily near 88.44 points, Ridge regularization pulls extreme predictions toward the population mean to minimize overall squared loss, systematically underpredicting 98-point wines and overpredicting 80-point wines."))

story.append(H2("D. What would have happened without de-duplication?"))
story.append(P("Without removing the 10,016 duplicate reviews, identical text entries would populate both training and test partitions. The model would memorize exact lexical combinations, yielding deceptively low test MAE and inflated R² that collapse when deployed on new unseen vintages."))

# Section 8: Conclusion
story.append(H("8. Conclusion"))
story.append(P("1. <b>Ridge regression on combined modalities</b> achieves R² = 0.7689 and MAE = 1.164 points.", 'B_Bullet'))
story.append(P("2. <b>Tasting notes contribute +18.89% explained variance</b> beyond price and origin metadata.", 'B_Bullet'))
story.append(P("3. <b>De-duplication eliminated 10,016 redundant reviews</b>, preventing severe data leakage.", 'B_Bullet'))

# AI Use Disclosure
story.append(H("AI Use Disclosure"))
story.append(P("Antigravity was utilized as a coding assistant for script templating, visualization scripting, and ReportLab PDF compilation. All experimental preprocessing pipelines, model selection, ablation design, and error interpretations were independently formulated, validated, and verified by the author."))

# References
story.append(H("References"))
story.append(P("[1] Z. Thoma, 'Wine Reviews Dataset,' Kaggle, 2017. [Online]. Available: kaggle.com/zynicide/wine-reviews.", 'B_Bullet'))
story.append(P("[2] F. Pedregosa et al., 'Scikit-learn: Machine Learning in Python,' <i>JMLR</i>, vol. 12, pp. 2825-2830, 2011.", 'B_Bullet'))
story.append(P("[3] A. E. Hoerl and R. W. Kennard, 'Ridge regression: Biased estimation for nonorthogonal problems,' <i>Technometrics</i>, 1970.", 'B_Bullet'))
story.append(P("[4] F. Galton, 'Regression towards mediocrity in hereditary stature,' <i>J. Anthropol. Inst.</i>, 1886.", 'B_Bullet'))

# Build document
doc = TwoColDoc(pdf_path)
doc.build(story)
print(f"Report successfully compiled: {pdf_path}")
