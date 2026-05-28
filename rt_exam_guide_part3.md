# Section 10-15: Fluoroscopy, Nuclear Medicine, Radiation Therapy, Contrast Media, QC, Law

---

# 📡 SECTION 10 — FLUOROSCOPY & INTERVENTIONAL RADIOLOGY

## 10.1 Fluoroscopy Physics

### Image Intensifier (II) — ระบบเก่า

**การทำงาน:**
1. X-ray กระทบ **Input phosphor** (Cesium Iodide: CsI) → แสง
2. **Photocathode** → แปลงแสงเป็น electron
3. **Electrostatic focusing** → เร่ง electron
4. **Output phosphor** → electron กระทบ → แสงสว่าง (ขนาดเล็กลง → intensity สูง)
5. Camera (CCD/optical) → video signal

**Brightness Gain = Flux Gain × Minification Gain**
- **Minification Gain** = (d_input/d_output)² = (23/2.3)² ≈ 100
- **Flux Gain** ≈ 50-100
- **Total brightness gain** ≈ 5,000-20,000 เท่า

**Image Intensifier Artifacts:**
| Artifact | สาเหตุ | ผล |
|---------|-------|-----|
| **Vignetting** | Brightness สูงตรงกลาง ต่ำที่ขอบ | ขอบมืดกว่ากลาง |
| **Pincushion distortion** | Electrostatic lens | เส้นตรงดูโค้ง (barrel distortion) |
| **S-distortion** | External magnetic field | ภาพบิดเป็น S |

### Flat Panel Detector (FPD) Fluoroscopy — ระบบใหม่
- ใช้ amorphous Silicon (a-Si) + CsI scintillator
- **ข้อดี:** ไม่มี vignetting, ไม่มี distortion, dynamic range กว้าง
- เป็นมาตรฐานในปัจจุบัน (C-arm, angio suite)

## 10.2 Fluoroscopy Modes

| Mode | Dose rate | ใช้เมื่อ |
|------|----------|---------|
| **Continuous fluoroscopy** | สูงสุด | Standard |
| **Pulsed fluoroscopy** | ลด 50-80% | ต้องการลด dose |
| **Last image hold (LIH)** | ไม่มี dose ขณะดู | ดู image โดยไม่เปิด beam |
| **Digital subtraction angiography (DSA)** | สูง | Angiography |

### Pulsed Fluoroscopy
- ปล่อย pulse 7.5, 15, 30 frames/sec (แทน continuous)
- ลด dose ได้ 50-75% เมื่อเทียบ continuous
- Image quality เล็กน้อยลดลงเมื่อ frame rate ต่ำ

## 10.3 Fluoroscopy Radiation Safety

### Patient Dose
- **Skin entrance dose rate:** 10-100 mGy/min (continuous)
- **Air kerma** ≥ 3 Gy → risk of radiation-induced skin injury
- **Radiation-induced skin injuries:**
  | Dose (Gy) | Effect | Onset |
  |----------|--------|-------|
  | 2 | Temporary epilation | 3 weeks |
  | 3 | Erythema | 1-2 weeks |
  | 6 | Moist desquamation | 2-3 weeks |
  | 10 | Ulceration | 3-6 weeks |
  | >20 | Necrosis | |

### Staff Dose ใน Fluoroscopy
- Staff dose สูงสุดในบรรดา diagnostic imaging ทั้งหมด
- **Distance จาก patient เป็น factor สำคัญที่สุด**
- **Protective equipment ที่ต้องใส่:**
  - Lead apron (0.5 mm Pb equivalent) ✓
  - Thyroid shield ✓
  - Lead glasses ✓ (ป้องกัน cataract)
  - Lead gloves (ถ้ามือใกล้ primary beam)
  - Lead curtain/drapes บน table

## 10.4 Interventional Radiology

### Common Procedures
| Procedure | หลักการ | Contrast |
|---------|---------|---------|
| **Angiography** | Catheter + contrast injection | Iodinated IV |
| **PTCA/PCI** | Balloon, stent ใน coronary | Iodinated |
| **ERCP** | Endoscope + fluoroscopy, bile duct | Iodinated |
| **IVP/Urography** | Uroกraph | Iodinated IV |
| **Myelography** | Contrast ใน subarachnoid space | Non-ionic, iso-osmolar |
| **Arthrography** | Contrast ใน joint space | Iodinated/Gadolinium |
| **Hysterosalpingography (HSG)** | Uterus, fallopian tube | Iodinated |
| **Barium Swallow** | Esophagus | Barium |
| **UGI Series** | Stomach, duodenum | Barium |
| **Barium Enema (BE)** | Colon | Barium |

### Sterile Technique ใน Interventional
- การเตรียม sterile field
- Surgical hand scrub
- Sterile gown, gloves
- Catheter, guidewire handling
- ห้ามข้าม sterile field

---

# ☢️ SECTION 11 — NUCLEAR MEDICINE

## 11.1 Radioisotopes ที่ต้องรู้

| Radionuclide | Half-life | Energy (keV) | Decay | ใช้ใน |
|-------------|---------|------------|------|------|
| **Tc-99m** | 6.02 hr | 140 keV | IT (isomeric transition) | Bone scan, thyroid, cardiac, renal, lung |
| **I-131** | 8.06 days | 364 keV | β⁻ + γ | Thyroid treatment, thyroid scan |
| **I-123** | 13.2 hr | 159 keV | EC + γ | Thyroid scan |
| **Ga-67** | 78 hr | 93, 184, 300 keV | EC + γ | Infection, tumor |
| **Tl-201** | 73 hr | 70-80 keV | EC + γ | Cardiac perfusion (เก่า) |
| **F-18 (FDG)** | 110 min | 511 keV (annihilation) | β⁺ | PET — glucose metabolism |
| **In-111** | 67 hr | 173, 247 keV | EC | WBC scan, Octreotide |
| **Rb-82** | 75 sec | 511 keV | β⁺ | PET cardiac perfusion |

### ⭐ Tc-99m — สำคัญที่สุดใน Nuclear Medicine
- เป็น **workhorse** ของ Nuclear Medicine (ใช้มากที่สุด)
- ได้จาก Mo-99/Tc-99m generator (cow)
- **ข้อดี:** Half-life 6 hr (สั้นพอ), 140 keV (เหมาะ gamma camera), pure gamma

## 11.2 Gamma Camera (Anger Camera)

### ส่วนประกอบ
1. **Collimator** — กรอง photon ให้ผ่านเฉพาะทิศที่ต้องการ
2. **NaI(Tl) crystal** — แปลง gamma → แสง
3. **Photomultiplier tube (PMT) array** — แปลงแสง → electrical signal
4. **Position logic** — คำนวณตำแหน่ง event
5. **Pulse height analyzer (PHA)** — กรองพลังงาน (energy window)

### Collimator Types
| ประเภท | ลักษณะ | ใช้กับ |
|-------|--------|------|
| **LEHR (Low Energy High Resolution)** | Hole เล็ก, ยาว | Tc-99m (140 keV) |
| **LEGP (Low Energy General Purpose)** | Hole กลาง | Tc-99m |
| **MEGP (Medium Energy)** | Hole กว้าง, ยาว | Ga-67, In-111 |
| **HEGP (High Energy)** | Hole ใหญ่มาก, หนามาก | I-131 (364 keV) |
| **Pinhole** | รู เดียว | Thyroid, small parts (magnify) |
| **Fan beam** | SPECT cardiac | Cardiac |

## 11.3 SPECT (Single Photon Emission CT)

- Gamma camera หมุนรอบผู้ป่วย → ได้ 3D data
- Reconstruction: Filtered Back Projection หรือ Iterative
- **Attenuation correction** สำคัญ (บริเวณ attenuation สูง เช่น diaphragm → false defect)

### SPECT Clinical Applications
| Scan | Radiopharmaceutical | Clinical use |
|------|---------------------|-------------|
| **Bone scan** | Tc-99m MDP | Metastasis, fracture |
| **Myocardial perfusion (MPI)** | Tc-99m Sestamibi/Tetrofosmin | Coronary artery disease |
| **Brain SPECT** | Tc-99m HMPAO | Dementia, epilepsy |
| **Renal scan** | Tc-99m DTPA/MAG3 | Renal function, obstruction |
| **Thyroid scan** | Tc-99m pertechnetate / I-123 | Nodule function (hot/cold) |
| **Lung scan (V/Q)** | Tc-99m MAA (perfusion) + Tc-99m DTPA aerosol (ventilation) | Pulmonary embolism |

## 11.4 PET (Positron Emission Tomography)

### หลักการ
- ฉีด β⁺ emitter (F-18 FDG)
- β⁺ + electron → **annihilation** → 2 photons 511 keV ทิศตรงข้าม
- **Coincidence detection** — รับ 2 photon พร้อมกัน → locate position

### PET Radiopharmaceuticals
| Tracer | Target | ใช้ดู |
|-------|--------|------|
| **F-18 FDG** | Glucose metabolism | Cancer staging, brain, cardiac |
| F-18 NaF | Bone | Bone metastasis |
| F-18 PSMA | PSMA receptor | Prostate cancer |
| Ga-68 DOTATATE | Somatostatin receptor | NET (neuroendocrine tumor) |
| Rb-82 | Perfusion | Cardiac PET |

### PET/CT vs PET/MRI
| | PET/CT | PET/MRI |
|--|--------|--------|
| Anatomical | CT (fast) | MRI (better soft tissue) |
| Attenuation correction | CT-based (accurate) | MRI-based (เพิ่งพัฒนา) |
| Radiation | เพิ่มจาก CT | น้อยกว่า |
| ใช้มาก | ส่วนใหญ่ | บางศูนย์ |

## 11.5 Radiation Safety ใน Nuclear Medicine

### Patient Excretion
- ผู้ป่วยขับ radioactivity ออกทาง urine, feces, sweat
- ต้องแนะนำ: ดื่มน้ำมาก, flush toilet หลายครั้ง, แยกจากเด็ก/หญิงตั้งครรภ์ชั่วคราว

### Staff Protection
- **ใช้ syringe shield** ขณะเตรียม/ฉีด dose
- **L-block shield** ขณะเตรียม radiopharmaceutical
- **Ring dosimeter** + **whole body dosimeter**
- **Contamination survey** หลังทำงาน

### Radioactive Waste
- เก็บรอ decay (decay in storage)
- Tc-99m → รอ 10 half-lives = 60 hours → ทิ้งได้
- I-131 → รอ 10 × 8 days = 80 วัน

---

# ⚡ SECTION 12 — RADIATION THERAPY

## 12.1 Types of Radiation Therapy

| ประเภท | วิธีการ | ตัวอย่าง |
|--------|--------|--------|
| **External beam RT (EBRT)** | เครื่องฉายรังสีภายนอก | LINAC |
| **Brachytherapy** | ใส่ source ใกล้/ในก้อนมะเร็ง | HDR, LDR |
| **Proton therapy** | Beam จาก proton accelerator | ใช้กับ pediatric, base of skull |
| **SBRT/SRS** | High dose ต่อครั้ง น้อยครั้ง | Brain, lung, liver |

## 12.2 Linear Accelerator (LINAC)

### ส่วนประกอบ LINAC
1. **Electron gun** — ปล่อย electron
2. **Waveguide** — เร่ง electron ด้วย microwave
3. **Bending magnet** — หัน electron beam 270°
4. **Target (W)** — ผลิต X-ray (bremsstrahlung) หรือ บาง LINAC ใช้ electron โดยตรง
5. **Flattening filter** — ทำ beam สม่ำเสมอ (หรือ FFF = Flattening Filter Free สำหรับ SBRT)
6. **Ion chamber (monitor chamber)** — วัด dose output
7. **Collimator (MLC)** — Multi-leaf collimator → กำหนดรูปร่าง beam

### Energy ของ LINAC
- **Photon:** 6 MV, 10 MV, 15 MV, 18 MV
- **Electron:** 4-20 MeV (ใช้รักษา superficial lesion)
- **ข้อแตกต่าง photon vs electron:**
  - Photon → penetrating → ลึก
  - Electron → dose สูงที่ depth ที่กำหนดแล้วลดฮวบ → ไม่ทะลุลึก

## 12.3 Fractionation

**หลักการ 4R ของ Radiobiology:**
1. **Repair** — เซลล์ปกติซ่อมแซมได้ดีกว่ามะเร็ง
2. **Redistribution** — เซลล์มะเร็งกระจายใน cell cycle
3. **Repopulation** — เซลล์ปกติฟื้นตัวระหว่าง fraction
4. **Reoxygenation** — hypoxic tumor cell ได้ O₂ → radiosensitive ขึ้น

### Fractionation Schedules
| ประเภท | Dose/fraction | จำนวน | Total dose | ตัวอย่าง |
|-------|-------------|--------|-----------|--------|
| Conventional | 1.8-2 Gy | 25-35 | 45-70 Gy | Breast, head & neck |
| Hypofractionation | >2 Gy | น้อยกว่า | ต่างกัน | Prostate, breast (some) |
| SBRT/SABR | 6-20 Gy | 1-5 | 24-60 Gy | Lung, liver, spine |
| SRS | 12-24 Gy | 1 | - | Brain met, AVM |
| Hyperfractionation | <1.8 Gy | >35 | สูงกว่า | H&N (เก่า) |

## 12.4 Treatment Planning

### Simulation
1. ผู้ป่วยอยู่ใน treatment position บน CT simulator
2. ถ่าย CT (simulation CT) → ส่ง TPS
3. วางอุปกรณ์ตรึง (immobilization): mask, body frame, vacuum bag

### Target Volume Definitions (ICRU)
| Volume | นิยาม |
|--------|------|
| **GTV (Gross Tumor Volume)** | ก้อน visible ใน imaging |
| **CTV (Clinical Target Volume)** | GTV + microscopic extension |
| **PTV (Planning Target Volume)** | CTV + margin for setup error + motion |
| **OAR (Organ at Risk)** | อวัยวะข้างเคียงที่ต้องป้องกัน |

### Dose Constraints (ตัวอย่าง)
| OAR | Constraint |
|-----|-----------|
| Spinal cord | Dmax < 45-50 Gy |
| Lens | Dmax < 5-10 Gy |
| Parotid gland | Mean < 26 Gy |
| Lung (mean) | < 20 Gy |
| Kidney | Mean < 18 Gy |

## 12.5 Brachytherapy

| ประเภท | Dose rate | ตัวอย่าง Source | ใช้กับ |
|-------|----------|--------------|------|
| **LDR (Low dose rate)** | 0.4-2 Gy/hr | Cs-137, I-125, Pd-103 | Prostate, cervix (ฝัง permanent) |
| **HDR (High dose rate)** | >12 Gy/hr | Ir-192 | Cervix, breast, bronchus |
| **PDR (Pulsed dose rate)** | กลางๆ | Ir-192 | เหมือน LDR แต่ pulsed |

### HDR Safety
- **Remote afterloading** — Source ถูกส่งอัตโนมัติ ไม่มีคนอยู่ในห้อง
- ห้อง treatment ต้องมี shielding เพียงพอ
- ต้องมี survey meter ก่อน-หลัง treatment

---

# 💉 SECTION 13 — CONTRAST MEDIA

## 13.1 Iodinated Contrast Media

### ประเภทของ Iodinated Contrast
| ประเภท | Osmolality | ตัวอย่าง | ข้อดี |
|-------|-----------|---------|------|
| **HOCM (High osmolar)** | ~1500-2000 mOsm/kg | Renografin, Conray | ราคาถูก |
| **LOCM (Low osmolar)** | ~500-800 mOsm/kg | Iohexol (Omnipaque), Iopamidol (Iopamiro) | Reaction น้อยกว่า |
| **Iso-osmolar (IOCM)** | ~290 mOsm/kg | Iodixanol (Visipaque) | Reaction น้อยสุด, ใช้ใน renal failure |

### Routes of Administration
- **IV** — CT, IVP, angiography
- **Intrathecal** — Myelography (ต้องใช้ non-ionic, iso-osmolar)
- **Intra-articular** — Arthrography
- **Oral** (diluted) — CT GI lumen
- **Rectal** — CT/fluoroscopy colon

## 13.2 Contrast Reactions

### Classification
| ระดับ | อาการ | การรักษา |
|------|------|---------|
| **Mild** | Urticaria, pruritus, nausea, flushing | Observation, antihistamine (Chlorpheniramine) |
| **Moderate** | Bronchospasm, hypotension, laryngeal edema, severe vomiting | O₂, IV fluid, Epinephrine 0.1-0.3 mL (1:1000 IM), Antihistamine, Salbutamol inhaler |
| **Severe (Anaphylaxis)** | Cardiovascular collapse, loss of consciousness, respiratory arrest | **Epinephrine 0.5 mL (1:1000) IM stat**, CPR, ACLS |

### Epinephrine Dose จำ:
- **Mild/Moderate:** 0.1-0.3 mL of 1:1000 IM
- **Severe:** 0.5 mL of 1:1000 IM (adult)
- เด็ก: 0.01 mg/kg (max 0.5 mg)

### Risk Factors สำหรับ Contrast Reaction
- Previous contrast reaction (สูงที่สุด — เพิ่ม 5-8 เท่า)
- Asthma
- Allergy ต่างๆ
- Cardiac disease
- Renal impairment

### Premedication Protocol (ผู้ป่วย high risk)
- **Elective:** Prednisone 50 mg oral ที่ 13, 7, 1 ชั่วโมงก่อน + Diphenhydramine 50 mg IM/oral 1 ชั่วโมงก่อน
- **Emergent:** Methylprednisolone 40 mg IV + Diphenhydramine 50 mg IV

## 13.3 Contrast-Induced Nephropathy (CIN) / Contrast-Induced AKI

**นิยาม:** creatinine เพิ่ม ≥0.5 mg/dL หรือ >25% จาก baseline ภายใน 48-72 ชั่วโมงหลังฉีด contrast

### Risk Factors
- Pre-existing renal insufficiency (**สำคัญที่สุด**)
- Diabetes mellitus + renal disease
- Dehydration
- Heart failure
- Multiple myeloma
- High dose contrast, HOCM

### Prevention
- **Hydration** (0.9% NaCl หรือ NaHCO₃) — ก่อนและหลังฉีด
- ใช้ contrast น้อยสุด, LOCM/IOCM
- หยุด Metformin 48 ชั่วโมงก่อนและหลัง (risk lactic acidosis ถ้า AKI)
- **N-acetylcysteine (NAC)** — ประโยชน์ยัง debate แต่ยังใช้ในบางสถาบัน
- eGFR threshold: **หยุดคิดระวัง** ถ้า eGFR < 30 mL/min/1.73m²

### ⭐ Metformin Protocol
- ผู้ป่วย DM ที่กิน Metformin + ตรวจ CT contrast:
  - ถ้า eGFR ≥ 30 → หยุด Metformin 48 ชั่วโมงหลังฉีด, ตรวจ Cr แล้วจึงเริ่มใหม่
  - ถ้า eGFR < 30 → พิจารณาไม่ฉีด contrast หรือปรึกษาแพทย์

## 13.4 Barium Contrast

### Barium Sulfate (BaSO₄)
- **ไม่ละลายน้ำ** → ปลอดภัยใน GI tract (ถ้าไม่รั่ว)
- **ห้ามใช้** ถ้าสงสัย perforation → barium peritonitis (fatal)
- ถ้าสงสัย perforation → ใช้ **water-soluble contrast** (Gastrografin) แทน

### Barium Studies
| Procedure | Preparation | Contrast |
|---------|-----------|---------|
| Barium swallow | NPO 4-6 hr | Ba suspension ความเข้มข้นปานกลาง |
| UGI Series | NPO midnight | Ba + glucagon (relax stomach) |
| Barium Enema | Bowel prep (Fleet enema) | Ba + air (double contrast) |
| Small bowel follow-through | Ba ดื่ม, ถ่ายภาพตามเวลา | Ba dilute |

## 13.5 Gadolinium (MRI Contrast)

### ประเภท
| ประเภท | ตัวอย่าง | NSF Risk |
|-------|---------|---------|
| **Linear ionic** | Magnevist (Gd-DTPA), Omniscan | **สูงสุด** |
| **Linear non-ionic** | Omniscan, OptiMARK | **สูง** |
| **Macrocyclic ionic** | Dotarem (Gd-DOTA) | **ต่ำมาก** |
| **Macrocyclic non-ionic** | ProHance, Gadavist | **ต่ำมาก** |

**สรุป:** Macrocyclic > Linear ในแง่ความปลอดภัย (NSF)

### Gadolinium Retention
- Gd สะสมใน brain (globus pallidus, dentate nucleus) ในระยะยาว
- ยังไม่ทราบผลกระทบที่ชัดเจน
- แนะนำใช้ dose ต่ำสุด, macrocyclic เมื่อจำเป็น

---

# 🔍 SECTION 14 — QUALITY CONTROL (QC/QA)

## 14.1 QC vs QA

| | QA (Quality Assurance) | QC (Quality Control) |
|--|----------------------|---------------------|
| ความหมาย | ระบบรวมที่รับประกันคุณภาพ | การทดสอบและวัดผลเฉพาะอย่าง |
| ขอบเขต | กว้าง (นโยบาย, training, review) | แคบ (test, measurement) |
| ตัวอย่าง | Accreditation program, peer review | kVp test, phantom test |

## 14.2 General Radiography QC

### Daily Tests
- **Reject/Repeat analysis** — ดูอัตรา reject ไม่เกิน 5%
- **Darkroom fog** (ถ้าใช้ film)
- **Screen cleanliness**

### Weekly Tests
- **Image quality (phantom)**

### Monthly Tests
- **Visual inspection** — ตรวจอุปกรณ์ทางกายภาพ

### Annual Tests (Physicist)
| Test | เกณฑ์ |
|-----|------|
| **kVp accuracy** | ±5% ของค่าตั้ง |
| **mAs linearity** | ±10% |
| **Timer accuracy** | ±5% |
| **HVL** | ≥ 2.3 mm Al ที่ 80 kVp |
| **Focal spot size** | ≤20% deviation |
| **Beam alignment** | ≤3% of SID |
| **AEC (Phototimer) reproducibility** | ±10% |
| **Radiation output reproducibility** | ±5% |

## 14.3 Repeat/Reject Analysis

**วัตถุประสงค์:** หาสาเหตุ repeat เพื่อลด patient dose และต้นทุน

**Reject rate ที่ยอมรับได้:** ≤ 4-8% (ขึ้นกับสถาบัน)

### สาเหตุ Repeat ที่พบบ่อย
1. Positioning error (~30%)
2. Exposure error (over/under ~25%)
3. Motion (~15%)
4. Artifact (~10%)
5. Others

## 14.4 Mammography QC (ACR Standards)

### Technologist Tests
| Test | Frequency | Criteria |
|------|-----------|---------|
| Darkroom cleanliness | Daily | ไม่มี artifact |
| Processor QC | Daily (ถ้าใช้ film) | ตาม control chart |
| Screen cleanliness | Weekly | ไม่มี artifact |
| **Phantom image** | Weekly | ≥4 fiber, ≥3 speck, ≥3 mass |
| Visual checklist | Monthly | ผ่านทุกรายการ |
| Repeat analysis | Quarterly | ≤2% |
| Compression | Semi-annual | 25-45 lbs (111-200 N) |

### Physicist Tests (Annual)
- Mammographic unit assembly evaluation
- kVp, HVL, beam quality
- **Average Glandular Dose** ≤ 3 mGy
- Focal spot
- Image quality

## 14.5 CT QC

### Daily
- **Warm-up** ของหลอด X-ray
- **Air calibration** (air scan)
- **Scout image review**

### Weekly
- **CT number accuracy** (water = 0 ± 7 HU)
- **Image noise**

### Monthly/Quarterly (Physicist)
- **Spatial resolution (MTF)**
- **Low contrast resolution**
- **Slice thickness**
- **Table index accuracy**
- **CTDI measurement**

## 14.6 Monitor QC (DICOM GSDF)

### DICOM GSDF (Grayscale Standard Display Function)
- มาตรฐาน calibration ของ monitor
- ทำให้ monitor ทุกเครื่องแสดง image เหมือนกัน

### Monitor Luminance Requirements
| ประเภท Monitor | Lmin | Lmax | CR (Contrast Ratio) |
|--------------|------|------|-------------------|
| **Primary (Diagnostic)** | ≥1 cd/m² | ≥250 cd/m² | ≥250:1 |
| **Secondary** | ≥1 | ≥100 | ≥100:1 |
| **Mobile** | ≥1 | ≥100 | ≥100:1 |

### Monitor QC Tests
| Test | Frequency | Tool |
|------|-----------|------|
| Luminance | Monthly | Photometer |
| GSDF calibration | Annually | Photometer + software |
| Artifact | Weekly | Visual |

---

# ⚖️ SECTION 15 — LAW, ETHICS, PROFESSIONAL

## 15.1 กฎหมายที่เกี่ยวข้อง

### พระราชบัญญัติวิชาชีพรังสีเทคนิค พ.ศ. 2543
- จัดตั้ง **สภาวิชาชีพรังสีเทคนิค (Radiologic Technology Council)**
- กำหนดขอบเขตวิชาชีพ (scope of practice)
- ออกและต่ออายุใบอนุญาต
- จรรยาบรรณวิชาชีพ

### ใบอนุญาตประกอบวิชาชีพ
- **อายุ:** 5 ปี
- **ต่ออายุ:** ต้องสะสม **CPD (Continuing Professional Development)** hours
- **ถูกเพิกถอน** ได้กรณี: ประพฤติผิดจรรยาบรรณ, ทุจริต, ขาดคุณสมบัติ

### กฎหมายด้านรังสี
- **พระราชบัญญัติพลังงานนิวเคลียร์เพื่อสันติ พ.ศ. 2559** (แทน พรบ.พลังงานปรมาณูฯ 2504)
- **สำนักงานปรมาณูเพื่อสันติ (OAP)** — กำกับดูแลการใช้รังสี

### กฎหมายคุ้มครองผู้ป่วย
- **พระราชบัญญัติสุขภาพแห่งชาติ พ.ศ. 2550** — สิทธิผู้ป่วย
- **สิทธิผู้ป่วย 10 ประการ** — สิทธิรับรู้ข้อมูล, ปฏิเสธการรักษา ฯลฯ

## 15.2 Patient Rights (สิทธิผู้ป่วย)

1. **สิทธิได้รับบริการ** ตามมาตรฐาน
2. **สิทธิได้รับข้อมูล** เกี่ยวกับการรักษา (informed consent)
3. **สิทธิปฏิเสธ** การรักษา
4. **สิทธิความเป็นส่วนตัว** และ confidentiality
5. **สิทธิร้องเรียน** เมื่อไม่ได้รับบริการที่เหมาะสม

## 15.3 Informed Consent

### องค์ประกอบ
1. **Disclosure** — แจ้งข้อมูลเพียงพอ
2. **Comprehension** — ผู้ป่วยเข้าใจ
3. **Voluntariness** — ตัดสินใจเอง ไม่ถูกบังคับ
4. **Competency** — ผู้ป่วยมีความสามารถตัดสินใจ
5. **Consent** — แสดงการยินยอม

### Special Situations
- **Minor (ผู้เยาว์):** ต้องได้รับ consent จาก parent/guardian
- **Emergency:** ยกเว้น consent ได้ (implied consent)
- **Incapacitated:** ต้องได้จาก legal guardian/next of kin
- **Research:** ต้องมี IRB approval + written informed consent

## 15.4 Confidentiality และ Privacy

- ข้อมูลผู้ป่วย (รวม DICOM images) เป็นข้อมูลส่วนบุคคล
- **PDPA (Personal Data Protection Act) พ.ศ. 2562** ในไทย
  - ต้องขออนุญาตก่อนใช้ข้อมูลส่วนบุคคล
  - ห้ามเปิดเผยโดยไม่ได้รับความยินยอม
- เปิดเผยได้เฉพาะ: ผู้ป่วยยินยอม, บุคลากรที่ดูแล, ตามคำสั่งศาล

## 15.5 จรรยาบรรณวิชาชีพรังสีเทคนิค

| หลัก | ความหมาย |
|-----|---------|
| **Beneficence** | กระทำเพื่อประโยชน์ผู้ป่วย |
| **Non-maleficence** | ไม่ทำให้ผู้ป่วยเสียหาย |
| **Autonomy** | เคารพสิทธิ์ผู้ป่วย |
| **Justice** | ให้บริการเท่าเทียม ไม่เลือกปฏิบัติ |
| **Veracity** | ซื่อสัตย์ ไม่หลอกลวง |
| **Fidelity** | รักษาคำมั่น ความไว้วางใจ |

## 15.6 Scope of Practice — สิ่งที่รังสีเทคนิคทำได้/ทำไม่ได้

| ทำได้ | ทำไม่ได้ |
|------|---------|
| ถ่ายภาพรังสีตาม order แพทย์ | สั่ง order ด้วยตัวเอง |
| ปรับ technique เพื่อ image quality | วินิจฉัยโรค |
| ฉีด contrast ตาม protocol ที่แพทย์กำหนด | ตัดสินใจฉีด contrast เอง |
| First aid เบื้องต้น | ประกอบวิชาชีพเวชกรรม |
| Explain procedure | Prescribe medications |

---

# 🎯 High-Yield Summary — Section 10-15

## Mnemonics สำคัญ

**Contrast Reaction ระดับ Severe: "EEE"**
- Epinephrine (IM stat)
- Emergency call (ขอความช่วยเหลือ)
- Elevate legs (ถ้า hypotension)

**Gadolinium Safety: "MACRO = SAFE"**
- Macrocyclic Gd → NSF risk ต่ำ → ปลอดภัยกว่า Linear

**4R ของ Radiobiology: "Really Repair Repopulate Reoxygenate"**
- Repair, Redistribution, Repopulation, Reoxygenation

**MRI Zone: "1234 ไกลไปใกล้ magnet"**
- Zone I (public) → Zone IV (magnet room)

## จุดที่คนชอบพลาด

1. **Barium + perforation** → ห้ามใช้ barium! ใช้ water-soluble (Gastrografin)
2. **Myelography** → ต้องใช้ **non-ionic, iso-osmolar** contrast เท่านั้น
3. **Gadolinium + eGFR <30** → NSF risk → macrocyclic เท่านั้น (หรือไม่ฉีด)
4. **Metformin** → หยุดก่อนฉีด contrast ถ้า renal ไม่ดี → lactic acidosis risk
5. **Reject rate** ยอมรับได้ ≤ 4-8% (ไม่ใช่ 0%)
6. **สภาวิชาชีพรังสีเทคนิค** ออก และต่ออายุใบอนุญาต (ไม่ใช่กระทรวงสาธารณสุข)
7. **MRI projectile** = Metal ferromagnetic ถูกดูดแรง → อันตราย (ไม่ใช่แค่ความร้อน)
8. **Epinephrine severe reaction** = 0.5 mL of 1:1000 IM (ไม่ใช่ IV bolus)
9. **Tc-99m half-life** = 6.02 ชั่วโมง (ไม่ใช่ 6 วัน)
10. **Phantom mammography** weekly → ≥4 fibers, ≥3 specks, ≥3 masses

## Mini Quiz Section 10-15

1. สาเหตุ S-distortion ใน II fluoroscopy คืออะไร? → **External magnetic field**
2. Contrast reaction severe — ยาสำคัญที่สุดคือ? → **Epinephrine 0.5 mL (1:1000) IM**
3. ผู้ป่วย DM กิน Metformin จะฉีด CT contrast → ต้องทำอะไร? → **หยุด Metformin, เช็ค renal function, hydrate**
4. Tc-99m ได้จากอะไร? → **Mo-99/Tc-99m generator**
5. SPECT ต่างจาก Planar imaging อย่างไร? → **SPECT ได้ 3D image จาก rotating camera**
6. PET ใช้หลักการอะไร? → **Coincidence detection ของ 511 keV annihilation photon**
7. SBRT/SRS ต่างจาก conventional fractionation อย่างไร? → **High dose/fraction, few fractions**
8. Myelography ต้องใช้ contrast ชนิดใด? → **Non-ionic, iso-osmolar (เช่น Iohexol)**
9. MRI Zone IV คืออะไร? → **Magnet room — ต้องผ่าน screening ทุกคน**
10. ใบอนุญาตวิชาชีพรังสีเทคนิคมีอายุกี่ปี? → **5 ปี**
