# Section 16-18: High-Yield Summary, Mock Exam, Crash Course

---

# 🏆 SECTION 16 — HIGH-YIELD EXAM SUMMARY

## 16.1 สูตรที่ต้องจำ (ออกสอบบ่อยมาก)

| สูตร | ชื่อ | ตัวแปร |
|-----|-----|-------|
| **I ∝ 1/D²** | Inverse Square Law | I=intensity, D=distance |
| **mAs₂ = mAs₁ × (SID₂/SID₁)²** | SID compensation | - |
| **MF = SID/SOD = SID/(SID-OID)** | Magnification Factor | SOD=source-object |
| **15% kVp Rule** | kVp-mAs equivalent | +15% kVp = ×2 mAs |
| **HU = (μ_tissue - μ_water)/μ_water × 1000** | Hounsfield Unit | μ=attenuation coeff |
| **Pitch = Table feed/Collimation** | CT Pitch | - |
| **H = D × Wr** | Equivalent dose | Wr=radiation weighting |
| **E = Σ(H_T × W_T)** | Effective dose | W_T=tissue weighting |
| **ω₀ = γ × B₀** | Larmor frequency | γ=42.58 MHz/T (H) |
| **HVL: I = I₀ × (½)^(x/HVL)** | Beam attenuation | - |
| **DLP = CTDI_vol × Scan Length** | CT dose | mGy·cm |
| **Grid Ratio = h/D** | Grid ratio | h=lead strip height |

### ตัวอย่างโจทย์คำนวณที่ออกสอบบ่อย

**โจทย์ 1:** ผู้ป่วยถ่ายภาพที่ SID 100 cm ใช้ mAs = 20 mAs ถ้าต้องการเพิ่ม SID เป็น 150 cm ต้องใช้ mAs เท่าใด?
**เฉลย:** mAs₂ = 20 × (150/100)² = 20 × 2.25 = **45 mAs**

**โจทย์ 2:** X-ray intensity ที่ 1 เมตร = 100 mR ถ้าเคลื่อนออกห่างเป็น 3 เมตร intensity เป็นเท่าใด?
**เฉลย:** I₂ = 100 × (1/3)² = 100/9 = **11.1 mR**

**โจทย์ 3:** HVL = 4 mm Al ถ้าใส่ filter หนา 12 mm จะเหลือ intensity กี่%?
**เฉลย:** I = I₀ × (½)^(12/4) = (½)³ = 1/8 = **12.5%**

**โจทย์ 4:** SID = 120 cm, OID = 20 cm → Magnification factor = ?
**เฉลย:** SOD = 120-20 = 100 cm → MF = 120/100 = **1.2** (ภาพใหญ่กว่าจริง 20%)

## 16.2 ตาราง Modality Comparison

| Modality | Radiation | Contrast | Speed | Bone | Soft Tissue | Cost | Indications หลัก |
|---------|----------|---------|-------|------|------------|------|-----------------|
| **X-ray** | Low-Med | Low-Med | เร็วมาก | ดี | ปานกลาง | ต่ำ | Chest, bone, abdomen |
| **Fluoroscopy** | Med-High | Med | Real-time | ปานกลาง | ปานกลาง | ปานกลาง | GI, interventional |
| **CT** | High | High | เร็ว | ดีมาก | ดี | ปานกลาง | Trauma, oncology, vascular |
| **MRI** | ไม่มี | สูง | ช้า | ปานกลาง | ดีที่สุด | สูง | Brain, spine, MSK, pelvis |
| **Ultrasound** | ไม่มี | ต่ำ | เร็ว | ไม่ดี | ดี | ต่ำ | Abdomen, pregnancy, thyroid |
| **Nuclear Medicine** | Med | N/A | ช้า | ปานกลาง | ปานกลาง | สูง | Bone scan, thyroid, cardiac |
| **PET/CT** | High | สูง | ปานกลาง | ปานกลาง | ปานกลาง | สูงมาก | Oncology staging, brain |
| **Mammography** | Low | ปานกลาง | เร็ว | N/A | ดี (breast) | ปานกลาง | Breast cancer screening |

## 16.3 ตาราง Artifact Summary

| Modality | Artifact | สาเหตุ | วิธีแก้ |
|---------|---------|-------|-------|
| X-ray | Grid cutoff | Grid misalignment | ปรับ grid/tube |
| X-ray | Quantum mottle | mAs ต่ำ | เพิ่ม mAs |
| X-ray | Motion | Patient movement | ลด time, immobilize |
| CR | Ghost image | Plate ไม่ถูก erase | Erase ใหม่ |
| CT | Beam hardening | Dense material | Software correction |
| CT | Ring artifact | Detector เสีย | Calibration |
| CT | Metal streak | Metal implant | MARS algorithm |
| MRI | Aliasing | FOV เล็ก | เพิ่ม FOV |
| MRI | Chemical shift | Fat-water frequency | Fat suppression |
| MRI | Susceptibility | Metal/air | GRE→SE, adjust |
| Mammo | Grid lines | Stationary grid | Bucky (moving grid) |
| Fluoro | Vignetting | II system | → FPD system |
| Fluoro | Pincushion | Electrostatic lens | Digital correction |

## 16.4 Radiation Dose Comparison

| การตรวจ | Effective Dose (mSv) |
|--------|---------------------|
| Chest X-ray PA | 0.02 |
| Dental X-ray | 0.005 |
| Hand X-ray | 0.001 |
| Lumbar spine AP | 1.5 |
| Pelvis AP | 0.7 |
| IVP | 2.5 |
| **Mammography (2 view)** | **0.4** |
| **CT Head** | **1-2** |
| **CT Chest** | **5-7** |
| **CT Abdomen/Pelvis** | **8-14** |
| **CT Coronary** | **5-15** |
| Background radiation (annual) | 2-3 |
| Occupational dose limit | 20/yr |

## 16.5 Contrast Reaction Management Table

| อาการ | Severity | การรักษา |
|------|---------|---------|
| Urticaria, pruritus | Mild | Observe, Chlorpheniramine 10 mg IM/IV |
| Nausea, vomiting | Mild | Observe, antiemetic ถ้าจำเป็น |
| Bronchospasm mild | Moderate | O₂, Salbutamol inhaler, Epinephrine 0.1 mg IM |
| Hypotension | Moderate | ยกขา, IV fluid 0.9% NaCl 1L rapid |
| Laryngeal edema | Severe | O₂, Epinephrine 0.5 mg IM stat |
| **Anaphylaxis** | **Severe** | **Epinephrine 0.5 mg (0.5 mL of 1:1000) IM stat, CPR** |
| Pulmonary edema | Severe | O₂, Furosemide, sit upright |
| Seizure | Severe | Protect airway, Diazepam 5-10 mg IV |

## 16.6 Radiosensitivity ลำดับจำ (Mnemonic: "Lily Goes By Getting Little Muscle")

```
Lymphocyte (สูงสุด) — L
Gonadal cells — G
Bone marrow — B
GI epithelium — G
Lens of eye — L
Muscle/Nerve (ต่ำสุด) — M
```

## 16.7 CT Window Settings — ต้องจำ

| Window | WW | WL | ดู |
|--------|----|----|---|
| **Brain** | 80 | 40 | Parenchyma |
| **Subdural** | 150-200 | 50-75 | Subdural hematoma |
| **Lung** | 1500-2000 | -600 | Lung parenchyma |
| **Bone** | 2000-4000 | 300-700 | กระดูก |
| **Soft tissue/Abdomen** | 350-400 | 40-60 | Organ |
| **Mediastinum** | 350-400 | 50 | Vessel, node |

## 16.8 MRI Signal Summary — T1 vs T2

| Tissue | T1 | T2 | จำง่ายๆ |
|--------|----|----|--------|
| Fat | **Bright** | Intermediate | Fat=T1 bright |
| Water/CSF | Dark | **Bright** | Water=T2 bright |
| Air/Cortical bone | Dark | Very dark | - |
| Acute blood (deoxy-Hb) | Intermediate | **Very dark** | - |
| Subacute blood (met-Hb) | **Bright** | **Bright** | - |
| Chronic blood (hemosiderin) | Dark | **Very dark** | - |
| Gadolinium enhancement | **Bright** | - | Gd=T1 bright |
| FLAIR | CSF dark | CSF suppressed | - |

## 16.9 Positioning Summary — ต้องจำ

| View | Position | CR Angle | แสดง |
|------|---------|---------|------|
| PA Chest | ยืน, หน้าชิด IR | ตั้งฉาก T7 | Lung, heart, diaphragm |
| AP Lordotic | Lean back / tube cephalad 15-20° | - | Lung apex |
| Waters | Prone, mento-orbital ⊥ IR | - | Maxillary sinus |
| Caldwell | PA, 15° caudal | 15° caudal | Frontal, ethmoid |
| Towne | AP, 30° caudal | 30° caudal | Occipital, foramen magnum |
| Odontoid | AP, mouth open | ตั้งฉาก | C1-C2, dens |
| Swimmer's | Lateral, arm up/down | ตั้งฉาก | C7-T1 |
| Oblique lumbar | 45° | ตั้งฉาก | Facet joints, Scottie dog |
| Scapular Y | เอียง 45-60° | ตั้งฉาก | Shoulder dislocation |
| Tunnel (knee) | Knee flex 40-50° | ตั้งฉาก tibia | Intercondylar notch |
| CC (mammo) | Superior → inferior | ตั้งฉาก | Medial breast |
| MLO (mammo) | เอียง 40-60° | ตาม pectoralis | Lateral breast, axilla |

---

# 📝 SECTION 17 — MOCK EXAM (150 ข้อ พร้อมเฉลยละเอียด)

## หมวด A: PHYSICS (ข้อ 1-40)

**ข้อ 1:** ถ้าเพิ่ม kVp จาก 80 เป็น 92 kVp ผลต่อ radiographic density คือ
- A. เพิ่มขึ้น 2 เท่า
- B. ลดลง 2 เท่า
- C. ไม่เปลี่ยนแปลง
- D. เพิ่มขึ้นเท่ากับการเพิ่ม mAs 2 เท่า

**เฉลย: D** — 15% kVp rule: เพิ่ม kVp 15% = เพิ่ม density เทียบเท่า mAs ×2 (80 → 92 ≈ 15%)

---

**ข้อ 2:** Inverse square law: ถ้า SID เพิ่มจาก 100 เป็น 200 cm intensity จะเปลี่ยนอย่างไร?
- A. ลดลง 2 เท่า
- B. ลดลง 4 เท่า
- C. เพิ่มขึ้น 2 เท่า
- D. เพิ่มขึ้น 4 เท่า

**เฉลย: B** — I ∝ 1/D² → (200/100)² = 4 → intensity ลด 4 เท่า

---

**ข้อ 3:** Heel effect ส่งผลให้ intensity ด้านใดสูงกว่า?
- A. Anode side
- B. Cathode side
- C. เท่ากันทั้งสองด้าน
- D. ขึ้นกับ kVp

**เฉลย: B** — Cathode side มี intensity สูงกว่าเนื่องจาก anode angle ดูดซับ photon บางส่วน

---

**ข้อ 4:** ปฏิกิริยาใดทำให้เกิด scatter radiation ที่เป็นปัญหาหลักต่อ image quality ในการถ่ายภาพรังสีทั่วไป?
- A. Photoelectric effect
- B. Compton scatter
- C. Coherent scatter
- D. Pair production

**เฉลย: B** — Compton scatter เกิดในช่วง kVp ที่ใช้งานทางคลินิก (>80 keV) และสร้าง scatter ที่รบกวน image

---

**ข้อ 5:** ค่า HVL ที่สูงขึ้นบ่งบอกถึง
- A. Beam quality ต่ำลง
- B. Beam ผ่านวัตถุได้ยากขึ้น
- C. Beam quality สูงขึ้น (harder beam)
- D. mAs เพิ่มขึ้น

**เฉลย: C** — HVL สูง = ต้องใช้วัสดุหนากว่าเพื่อลด intensity ครึ่งหนึ่ง = beam คุณภาพสูง (penetrating กว่า)

---

**ข้อ 6:** Rotating anode มีข้อดีหลักคือ
- A. เพิ่ม spatial resolution
- B. ลด focal spot size
- C. กระจาย heat ได้มากกว่า → รับกระแสสูงกว่า
- D. ลด patient dose

**เฉลย: C** — การหมุนทำให้ electron กระจายทั่ว track → ทน heat load สูงกว่า stationary anode

---

**ข้อ 7:** Bremsstrahlung radiation มีลักษณะ spectrum แบบใด?
- A. Discrete (specific energies)
- B. Continuous (0 ถึง max kVp)
- C. Monoenergetic
- D. เฉพาะที่ characteristic energies

**เฉลย: B** — Bremsstrahlung = continuous spectrum จาก 0 ถึง max kVp ที่ตั้ง

---

**ข้อ 8:** เซลล์ใดมี radiosensitivity สูงสุด?
- A. Nerve cell
- B. Muscle cell
- C. Lymphocyte
- D. Liver cell

**เฉลย: C** — Lymphocyte มี radiosensitivity สูงสุดตาม Bergonie-Tribondeau law (mitotic, undifferentiated)

---

**ข้อ 9:** Photoelectric effect เกิดได้บ่อยเมื่อ
- A. พลังงานสูง + Z ต่ำ
- B. พลังงานต่ำ + Z สูง
- C. พลังงานสูง + Z สูง
- D. พลังงานต่ำ + Z ต่ำ

**เฉลย: B** — Photoelectric ∝ Z³/E³ → พลังงานต่ำและ Z สูงทำให้เกิดมากที่สุด

---

**ข้อ 10:** Dose limit สำหรับบุคลากรรังสีต่อปีตามมาตรฐาน ICRP คือ
- A. 5 mSv
- B. 10 mSv
- C. 20 mSv
- D. 50 mSv

**เฉลย: C** — ICRP recommends 20 mSv/year (averaged over 5 years, max 50 mSv in any single year)

---

**ข้อ 11:** Grid ratio 12:1 เหมาะกับ kVp range ใด?
- A. <70 kVp
- B. 70-90 kVp
- C. 90-110 kVp
- D. 110-125 kVp

**เฉลย: D** — Grid ratio 12:1 → 110-125 kVp

---

**ข้อ 12:** Characteristic X-ray เกิดจาก
- A. Electron เคลื่อนที่ผ่านใกล้ nucleus → เปลี่ยนทิศ
- B. Electron ใน outer shell มาแทนที่ inner shell → ปล่อย photon
- C. Photon ทำให้ electron หลุด → คืน energy
- D. Proton ชน electron → สร้าง positron

**เฉลย: B** — Characteristic X-ray เกิดเมื่อ outer shell electron มาแทน inner shell vacancy → ปล่อย photon พลังงาน = ผลต่าง binding energy

---

**ข้อ 13:** SID = 150 cm, OID = 30 cm → Magnification factor คือ
- A. 1.0
- B. 1.25
- C. 1.5
- D. 2.0

**เฉลย: B** — SOD = 150-30 = 120 cm → MF = 150/120 = **1.25**

---

**ข้อ 14:** mAs เพิ่มขึ้น 2 เท่า ส่งผลต่ออะไรบ้าง?
- A. Density เพิ่ม, contrast เพิ่ม
- B. Density เพิ่ม, contrast ไม่เปลี่ยน
- C. Density เพิ่ม, contrast ลด
- D. Density ลด, contrast เพิ่ม

**เฉลย: B** — mAs ควบคุม quantity ของ X-ray → density เพิ่ม แต่ contrast ไม่เปลี่ยน (contrast ควบคุมโดย kVp)

---

**ข้อ 15:** Upside-down focused grid ทำให้เกิดอะไร?
- A. Uniform density ลดลงทั้งภาพ
- B. ด้านซ้ายมืดกว่าด้านขวา
- C. ตรงกลางสว่าง ขอบมืดทั้งสองด้าน
- D. ภาพสว่างสม่ำเสมอ

**เฉลย: C** — Upside-down focused grid → bilateral cutoff (ขอบมืด) ตรงกลางสว่าง เนื่องจาก lead strip เอียงผิดทิศ

---

**ข้อ 16:** Deterministic effect ของรังสีมีลักษณะอย่างไร?
- A. ไม่มี threshold dose
- B. มี threshold dose และความรุนแรง ∝ dose
- C. เพิ่มโอกาสเกิด cancer ตาม dose
- D. เกิดเฉพาะในเซลล์สืบพันธุ์

**เฉลย: B** — Deterministic = มี threshold และ severity ∝ dose (เช่น erythema, cataract)

---

**ข้อ 17:** ทารกในครรภ์ระยะใดที่ไวต่อรังสีและ mental retardation มากที่สุด?
- A. 0-2 สัปดาห์
- B. 2-8 สัปดาห์
- C. 8-15 สัปดาห์
- D. 16-40 สัปดาห์

**เฉลย: C** — ระยะ 8-15 สัปดาห์ (fetal neuronal migration) เป็น radiosensitive ที่สุดสำหรับ mental retardation

---

**ข้อ 18:** หน่วย Sievert ใช้วัดอะไร?
- A. Absorbed dose
- B. Exposure
- C. Equivalent/Effective dose
- D. Activity

**เฉลย: C** — Sievert = หน่วยของ Equivalent dose (H) และ Effective dose (E)

---

**ข้อ 19:** การใช้ TLD dosimeter มีข้อดีหลักคือ
- A. อ่านได้ real-time ทันที
- B. ราคาถูกมาก
- C. Accurate, reusable, เล็ก
- D. ไม่ต้องส่งแล็บ

**เฉลย: C** — TLD: Thermoluminescent dosimeter มีความแม่นยำสูง, ใช้ซ้ำได้, ขนาดเล็ก แต่ต้องส่งแล็บอ่าน

---

**ข้อ 20:** Reciprocity law ในการถ่ายภาพรังสีหมายความว่า
- A. mA เท่ากัน → density เท่ากันเสมอ
- B. mAs เท่ากัน → density เท่ากัน ไม่ว่า mA/time combination ใด
- C. kVp เท่ากัน → exposure เท่ากัน
- D. SID เท่ากัน → density เท่ากัน

**เฉลย: B** — Reciprocity law: density ขึ้นกับ mAs รวม ไม่ใช่ mA หรือ time แยกกัน

---

**ข้อ 21:** LD50/30 ในมนุษย์คือประมาณเท่าใด?
- A. 0.5 Gy
- B. 3-5 Gy
- C. 10 Gy
- D. 20 Gy

**เฉลย: B** — LD50/30 ของมนุษย์ ≈ 3-5 Gy (whole body dose ที่ทำให้ 50% เสียชีวิตใน 30 วัน)

---

**ข้อ 22:** Pair production เกิดขึ้นที่พลังงานขั้นต่ำเท่าใด?
- A. 0.51 MeV
- B. 1.02 MeV
- C. 10 MeV
- D. 100 keV

**เฉลย: B** — Pair production ต้องการพลังงาน ≥ 1.02 MeV (mass equivalence ของ electron + positron = 2 × 0.511 MeV)

---

**ข้อ 23:** HVL ของ beam ถ้าต้องการให้ intensity เหลือ 12.5% ต้องผ่าน material กี่ HVL?
- A. 2 HVL
- B. 3 HVL
- C. 4 HVL
- D. 5 HVL

**เฉลย: B** — (½)³ = 1/8 = 12.5% → ต้องผ่าน 3 HVL

---

**ข้อ 24:** ปัจจัยใดที่ทำให้ image contrast ลดลง?
- A. เพิ่ม kVp
- B. ลด mAs
- C. ลด SID
- D. ใช้ grid

**เฉลย: A** — kVp สูง → compton scatter เพิ่ม → contrast ลด (long scale contrast)

---

**ข้อ 25:** Quantum mottle (noise) ใน digital radiography เกิดจาก
- A. kVp สูงเกินไป
- B. mAs น้อยเกินไป (photon น้อย)
- C. SID ยาวเกินไป
- D. Grid ratio ต่ำเกินไป

**เฉลย: B** — Quantum mottle = statistical fluctuation ของ photon → เกิดเมื่อ photon น้อย (mAs ต่ำ)

---

**ข้อ 26:** Coherent (Rayleigh) scatter มีนัยสำคัญทางคลินิกอย่างไร?
- A. สร้าง image fog สำคัญมาก
- B. เพิ่ม patient dose มาก
- C. มีนัยสำคัญน้อยมากในการถ่ายภาพรังสีทั่วไป
- D. เกิดที่พลังงานสูง (>100 keV)

**เฉลย: C** — Coherent scatter เกิดที่พลังงานต่ำมาก (<10 keV) ซึ่งถูกกรองออกโดย filtration → มีผลน้อยมาก

---

**ข้อ 27:** ค่า Gyromagnetic ratio ของ Hydrogen (¹H) ใน MRI คือ
- A. 26.75 MHz/T
- B. 42.58 MHz/T
- C. 100 MHz/T
- D. 63.87 MHz/T

**เฉลย: B** — γ (H-1) = 42.58 MHz/T (Larmor frequency ที่ 1T = 42.58 MHz)

---

**ข้อ 28:** Dose creep ในระบบ digital radiography หมายถึง
- A. Patient dose ลดลงเรื่อยๆ
- B. Technologist ค่อยๆ เพิ่ม exposure เพื่อ image quality โดยไม่จำเป็น
- C. Detector sensitivity ลดลงตามอายุ
- D. mAs ลดลงอัตโนมัติ

**เฉลย: B** — Dose creep = การค่อยๆ เพิ่ม mAs เพราะ digital ยังให้ภาพดู OK → dose เพิ่มโดยไม่จำเป็น

---

**ข้อ 29:** หลอด X-ray ทั่วไปใช้วัสดุ target ชนิดใด?
- A. Molybdenum (Mo)
- B. Rhodium (Rh)
- C. Tungsten (W)
- D. Copper (Cu)

**เฉลย: C** — Tungsten (W, Z=74) ใช้เป็น target ใน general X-ray tube เพราะ high Z, high melting point

---

**ข้อ 30:** ใน CT, pitch = 2 หมายความว่า
- A. Detector row 2 แถว
- B. Table เคลื่อน 2× collimation per rotation → gap
- C. กระแส X-ray 2 เท่า
- D. Slice thickness 2× บาง

**เฉลย: B** — Pitch = table feed/collimation. Pitch > 1 → gap ระหว่าง spiral → ลด dose แต่ image quality เล็กน้อยลด

---

**ข้อ 31:** HU ของน้ำ (water) ใน CT คือ
- A. -1000
- B. 0
- C. +50
- D. +100

**เฉลย: B** — Water = 0 HU (reference point ของ Hounsfield scale)

---

**ข้อ 32:** CT window: WW = 1500, WL = -600 ใช้ดูอะไร?
- A. Brain parenchyma
- B. Lung
- C. Bone
- D. Abdomen soft tissue

**เฉลย: B** — Lung window: WW 1500-2000, WL -600 to -700 → เห็น lung parenchyma, air, interstitium

---

**ข้อ 33:** Compton scatter เกิดมากเมื่อ
- A. พลังงาน X-ray ต่ำ + Z สูง
- B. พลังงาน X-ray สูง + soft tissue
- C. พลังงาน X-ray ต่ำ + กระดูก
- D. พลังงาน X-ray สูง + กระดูก

**เฉลย: B** — Compton เกิดกับ outer shell electron → predominant ใน soft tissue ที่ energy ปานกลาง-สูง

---

**ข้อ 34:** ข้อใดถูกต้องเกี่ยวกับ Stochastic effect?
- A. มี threshold dose ที่ชัดเจน
- B. ความรุนแรงขึ้นกับ dose
- C. โอกาสเกิด ∝ dose ไม่มี threshold
- D. เป็น deterministic effect อีกชื่อ

**เฉลย: C** — Stochastic = ไม่มี threshold, โอกาสเกิดขึ้นกับ dose แต่ความรุนแรงไม่ขึ้นกับ dose (cancer, leukemia)

---

**ข้อ 35:** Inherent filtration ของหลอด X-ray ทั่วไปเท่ากับประมาณ
- A. 0.1 mm Al
- B. 0.5-1.0 mm Al
- C. 2.5 mm Al
- D. 5 mm Al

**เฉลย: B** — Inherent filtration ≈ 0.5-1.0 mm Al equivalent (glass envelope + oil + window)

---

**ข้อ 36:** DQE (Detective Quantum Efficiency) คืออะไร?
- A. จำนวน photon ต่อ mAs
- B. ประสิทธิภาพของ detector ในการแปลง X-ray เป็น signal ที่ใช้งานได้
- C. ขนาดของ focal spot
- D. ความเร็ว scan ของ detector

**เฉลย: B** — DQE = SNR²_out / SNR²_in → วัดประสิทธิภาพ detector (DR > CR > Film)

---

**ข้อ 37:** mAs ที่ต้องใช้เมื่อเพิ่ม SID จาก 100 เป็น 150 cm (เดิมใช้ 40 mAs) คือ
- A. 60 mAs
- B. 90 mAs
- C. 27 mAs
- D. 80 mAs

**เฉลย: B** — mAs₂ = 40 × (150/100)² = 40 × 2.25 = **90 mAs**

---

**ข้อ 38:** ข้อใดถูกต้องเกี่ยวกับ Line Focus Principle?
- A. Actual focal spot เล็กกว่า effective focal spot
- B. Effective focal spot เล็กกว่า actual focal spot
- C. Actual = Effective เสมอ
- D. Anode angle ไม่ส่งผลต่อ focal spot

**เฉลย: B** — Line focus principle: anode angle ทำให้ effective focal spot (ที่มองจาก beam direction) เล็กกว่า actual focal spot

---

**ข้อ 39:** ปัจจัยใดที่เพิ่ม scatter radiation ในการถ่ายภาพรังสี?
- A. เพิ่ม grid ratio
- B. ลด kVp
- C. เปิด collimation กว้าง (large field size)
- D. ลด patient thickness

**เฉลย: C** — Field size ใหญ่ → volume ของ tissue ที่รับ irradiation มาก → scatter เพิ่ม

---

**ข้อ 40:** ค่าขีดจำกัดปริมาณรังสีสำหรับหญิงตั้งครรภ์ที่ประกาศการตั้งครรภ์ (declared pregnant worker) คือ
- A. 20 mSv/yr
- B. 5 mSv ตลอดการตั้งครรภ์
- C. 1 mSv ตลอดการตั้งครรภ์ (ICRP)
- D. เท่ากับบุคลากรทั่วไป

**เฉลย: C** — ICRP: ≤1 mSv ตลอดการตั้งครรภ์ (บางมาตรฐาน ≤5 mSv แต่ ICRP = 1 mSv)

---

## หมวด B: POSITIONING & ANATOMY (ข้อ 41-80)

**ข้อ 41:** PA Chest ถ่ายที่ SID เท่าใด?
- A. 100 cm
- B. 120 cm
- C. 150 cm
- D. 180 cm

**เฉลย: D** — PA Chest ใช้ **180 cm SID** เพื่อลด magnification ของ heart

---

**ข้อ 42:** Waters view (Parietoacanthial) แสดง sinus ใดได้ชัดที่สุด?
- A. Frontal sinus
- B. Ethmoid sinus
- C. Maxillary sinus
- D. Sphenoid sinus

**เฉลย: C** — Waters view = Maxillary sinus (จำ: "Waters = น้ำ = maxillary ที่ล้างหน้า")

---

**ข้อ 43:** Towne view ใช้ tube angle เท่าใด?
- A. 15° cephalad
- B. 15° caudad
- C. 30° caudad
- D. 30° cephalad

**เฉลย: C** — Towne view: AP position, tube 30° caudad → แสดง occipital bone, foramen magnum

---

**ข้อ 44:** Oblique lumbar spine แสดง "Scottie dog" anatomy อะไรคือ "pars interarticularis"?
- A. Eye
- B. Ear
- C. Neck
- D. Nose

**เฉลย: C** — Neck = pars interarticularis → collar on Scottie dog = spondylolysis (pars fracture)

---

**ข้อ 45:** ใน PA chest, ถ้าภาพ rotate ซ้ายออก — spinous process จะอยู่ตำแหน่งใด?
- A. กึ่งกลาง
- B. เยื้องไปทางซ้าย
- C. เยื้องไปทางขวา
- D. ไม่เปลี่ยน

**เฉลย: B** — Rotation ซ้ายออก → spinous process เยื้องไปทางซ้าย (ด้าน away from detector)

---

**ข้อ 46:** Swimmer's view (Twining) ใช้เมื่อใด?
- A. เห็น C1-C2 ไม่ชัด
- B. เห็น C7-T1 junction ไม่ได้ใน lateral
- C. เห็น skull base ไม่ชัด
- D. เห็น facet joint ไม่ชัด

**เฉลย: B** — Swimmer's = แก้ปัญหา C7-T1 ที่มัก obscure โดย shoulder

---

**ข้อ 47:** ใน CT brain, HU ของ acute hemorrhage คือ
- A. 0-15 HU
- B. 20-30 HU
- C. 50-90 HU
- D. >400 HU

**เฉลย: C** — Acute blood (deoxyhemoglobin) = **50-90 HU** → hyperdense ใน CT

---

**ข้อ 48:** AP chest ต่างจาก PA chest อย่างไรในแง่ heart size?
- A. Heart ดูเล็กกว่า
- B. Heart ดูใหญ่กว่า (magnified)
- C. ขนาดเท่ากัน
- D. ขึ้นกับ kVp

**เฉลย: B** — AP chest: heart อยู่ห่าง detector มากกว่า → OID มากกว่า → magnification สูงกว่า → heart ดูใหญ่กว่า

---

**ข้อ 49:** BI-RADS category 3 หมายถึงอะไร?
- A. Negative — routine screening
- B. Probably benign — short-interval follow-up
- C. Suspicious — recommend biopsy
- D. Highly suspicious

**เฉลย: B** — BI-RADS 3 = probably benign → follow up ใน 6 เดือน (ไม่ใช่ biopsy ทันที)

---

**ข้อ 50:** ใน MLO mammography, anatomy ใดต้องเห็นจึงถือว่า adequate?
- A. Nipple ใน profile
- B. Pectoralis muscle ถึงระดับ nipple
- C. Inframammary fold ชัด
- D. ทั้ง A, B, C

**เฉลย: D** — MLO ที่ดีต้องเห็น: nipple in profile + pectoralis muscle ถึง nipple level + IMF open

---

**ข้อ 51:** Cardiothoracic ratio (CTR) ปกติไม่เกิน
- A. 0.3
- B. 0.5
- C. 0.7
- D. 1.0

**เฉลย: B** — CTR ปกติ < **0.5** (ความกว้าง heart ไม่เกิน 50% ของ chest width ใน PA view)

---

**ข้อ 52:** Left lateral decubitus abdomen ใช้ตรวจสิ่งใด?
- A. Left pleural effusion
- B. Free air ที่ขอบตับ (right side)
- C. Renal calculi
- D. Bowel obstruction ใน small bowel

**เฉลย: B** — Left lateral decubitus: free air ลอยด้าน right (ที่อยู่บน) → เห็น free air ข้างตับ

---

**ข้อ 53:** ใน MRI, FLAIR sequence มีประโยชน์อะไร?
- A. Suppress fat → เห็น edema ชัด
- B. Suppress CSF → เห็น periventricular lesion ชัด
- C. Enhance blood vessel
- D. Detect calcification

**เฉลย: B** — FLAIR = Fluid Attenuated Inversion Recovery → suppress CSF → ดี detect lesion ติดกับ ventricle

---

**ข้อ 54:** Diffusion Weighted Image (DWI) bright (restricted diffusion) พบในอะไร?
- A. Vasogenic edema
- B. Hemorrhage เก่า
- C. Acute ischemic stroke
- D. Normal brain parenchyma

**เฉลย: C** — Acute ischemic stroke → cytotoxic edema → cell membrane breakdown → restricted water diffusion → DWI bright

---

**ข้อ 55:** Hip AP: lower limb ต้องอยู่ในท่าใด?
- A. External rotation 15°
- B. Internal rotation 15°
- C. ตั้งตรง (neutral)
- D. Flexion 30°

**เฉลย: B** — Hip AP: internal rotation 15° → femoral neck ไม่ overlap → เห็น neck ชัด

---

**ข้อ 56:** Hepatic segments ตาม Couinaud, segment ใดอยู่ใกล้ IVC มากที่สุด?
- A. Segment II
- B. Segment IV
- C. Segment I (Caudate lobe)
- D. Segment VII

**เฉลย: C** — Caudate lobe (Segment I) อยู่ระหว่าง IVC และ ligamentum venosum

---

**ข้อ 57:** MRI ที่ 3 Tesla Larmor frequency ของ Hydrogen คือ
- A. 42.58 MHz
- B. 63.87 MHz
- C. 127.74 MHz
- D. 200 MHz

**เฉลย: C** — ω₀ = γ × B₀ = 42.58 × 3 = **127.74 MHz**

---

**ข้อ 58:** Odontoid process view (Open mouth) แสดง vertebra ระดับใด?
- A. C3-C4
- B. C1-C2 (atlas-axis)
- C. C5-C6
- D. C7-T1

**เฉลย: B** — Open mouth view = C1 (atlas) และ C2 (axis/odontoid process/dens)

---

**ข้อ 59:** Scapular Y-view ใช้ดูอะไร?
- A. Scapular fracture
- B. Rotator cuff tear
- C. Shoulder dislocation (anterior vs posterior)
- D. AC joint injury

**เฉลย: C** — Scapular Y-view: normal = humeral head ตรงกลาง Y; anterior dislocation = หน้า coracoid

---

**ข้อ 60:** Conus medullaris ของ spinal cord ปกติสิ้นสุดที่ระดับใดในผู้ใหญ่?
- A. T10-T11
- B. L1-L2
- C. L3-L4
- D. S1-S2

**เฉลย: B** — Conus medullaris สิ้นสุดที่ **L1-L2** ในผู้ใหญ่ (เด็กแรกเกิด L2-L3)

---

**ข้อ 61:** CT Abdomen arterial phase ถ่ายที่เวลาใดหลังฉีด contrast?
- A. 5-10 วินาที
- B. 25-35 วินาที
- C. 60-70 วินาที
- D. 3-5 นาที

**เฉลย: B** — Arterial phase = **25-35 วินาที** หลัง contrast injection

---

**ข้อ 62:** DWI ใน MRI: ADC map dark หมายถึง
- A. Free diffusion
- B. Restricted diffusion (ischemia, abscess)
- C. Normal brain
- D. Vasogenic edema

**เฉลย: B** — ADC dark = low ADC = restricted diffusion (cytotoxic edema, abscess, hypercellular tumor)

---

**ข้อ 63:** Caldwell view ใช้ tube angle เท่าใด?
- A. 15° cephalad
- B. 15° caudad
- C. 30° caudad
- D. ตั้งฉาก

**เฉลย: B** — Caldwell = PA, **15° caudad** → Frontal sinus, ethmoid sinus

---

**ข้อ 64:** Celiac axis (Celiac trunk) แยกจาก aorta ที่ระดับใด?
- A. T10-T11
- B. T12-L1
- C. L1-L2
- D. L3

**เฉลย: B** — Celiac axis origin ≈ **T12-L1** → แยกเป็น Splenic A, Common hepatic A, Left gastric A

---

**ข้อ 65:** ใน breast density category ใดที่ mammography sensitivity ต่ำที่สุด?
- A. Category A (almost entirely fatty)
- B. Category B (scattered)
- C. Category C (heterogeneous)
- D. Category D (extremely dense)

**เฉลย: D** — Dense breast (Category D) ทำให้ sensitivity ของ mammography ต่ำที่สุด

---

**ข้อ 66:** Breathing technique ใน thoracic spine lateral ทำเพื่ออะไร?
- A. ลด patient dose
- B. Blur ribs → เห็น vertebra ชัดขึ้น
- C. ลด motion artifact ของ spine
- D. เพิ่ม lung volume

**เฉลย: B** — Breathing (aeration) technique: ผู้ป่วยหายใจปกติระหว่าง long exposure → ribs และ sternum blur ออก → vertebra ชัด

---

**ข้อ 67:** ใน CT brain, window ใดใช้ดู subdural hematoma ได้ชัดที่สุด?
- A. Brain window (WW 80, WL 40)
- B. Subdural window (WW 150, WL 75)
- C. Bone window (WW 4000, WL 400)
- D. Lung window

**เฉลย: B** — Subdural window (WW 150, WL 75) → เห็น isodense/hyperdense SDH ชัดขึ้น

---

**ข้อ 68:** Minification gain ของ Image Intensifier คำนวณจาก
- A. (d_input/d_output)
- B. (d_input/d_output)²
- C. d_output/d_input
- D. Flux gain × Contrast ratio

**เฉลย: B** — Minification gain = (diameter_input / diameter_output)²

---

**ข้อ 69:** ใน thoracic spine, กี่ซี่ ribs ที่ articulate กับ sternum (true ribs)?
- A. 5 pairs
- B. 7 pairs
- C. 10 pairs
- D. 12 pairs

**เฉลย: B** — Ribs 1-7 = True ribs (articulate กับ sternum โดยตรง)

---

**ข้อ 70:** Knee tunnel view (Intercondylar fossa) ใช้ knee angle เท่าใด?
- A. 20°
- B. 40-50°
- C. 90°
- D. 120°

**เฉลย: B** — Tunnel view: knee flex **40-50°**, CR ตั้งฉากกับ tibia → เห็น intercondylar fossa, posterior femoral condyle

---

**ข้อ 71:** ใน MRI, T2*-weighted GRE ดีกว่า conventional SE ในการตรวจ
- A. White matter lesion
- B. Hemorrhage และ calcification
- C. Cartilage tear
- D. Fat content

**เฉลย: B** — T2* GRE sensitive ต่อ susceptibility effects → ดี detect hemosiderin, calcification

---

**ข้อ 72:** SMA (Superior Mesenteric Artery) origin อยู่ที่ระดับใด?
- A. T12
- B. L1
- C. L2
- D. L3

**เฉลย: B** — SMA origin ≈ **L1** (ต่ำกว่า celiac axis เล็กน้อย)

---

**ข้อ 73:** Mammographic average glandular dose (AGD) ไม่ควรเกิน
- A. 1 mGy
- B. 3 mGy
- C. 5 mGy
- D. 10 mGy

**เฉลย: B** — ACR standard: AGD ≤ **3 mGy** ต่อ view (standard breast)

---

**ข้อ 74:** ใน AP pelvis ถ้า obturator foramen ขวาใหญ่กว่าซ้าย บ่งบอกอะไร?
- A. Rotation ขวาออก
- B. Rotation ซ้ายออก
- C. Lordosis มาก
- D. ปกติ

**เฉลย: A** — Obturator foramen ด้านที่ rotate ออก (away from IR) จะดูใหญ่กว่า

---

**ข้อ 75:** CTDI_vol หน่วยคือ
- A. mGy
- B. mGy·cm
- C. mSv
- D. mGy/mAs

**เฉลย: A** — CTDI_vol หน่วยเป็น **mGy** (DLP = CTDI_vol × cm = mGy·cm)

---

**ข้อ 76:** ถ้า Scottie dog มี "collar" (radiolucent line ที่ neck) หมายถึง
- A. Spondylolisthesis
- B. Spondylolysis (pars interarticularis fracture)
- C. Facet joint arthritis
- D. Disc herniation

**เฉลย: B** — Collar sign ใน oblique lumbar = **spondylolysis** (fracture ที่ pars interarticularis = neck of Scottie dog)

---

**ข้อ 77:** ใน lateral chest, right lateral vs left lateral มีข้อแตกต่างอย่างไร?
- A. Left lateral: magnify right side, ใช้ดู right lesion
- B. Left lateral: left ใกล้ detector → left side sharp; ใช้เมื่อ suspect left-sided lesion
- C. ไม่แตกต่างกัน
- D. Right lateral เสมอสำหรับ chest

**เฉลย: B** — Left lateral: left chest ใกล้ IR → less magnification ด้านซ้าย → ใช้เมื่อ left-sided lesion (standard คือ left lateral เพราะ heart ชิด IR ลด magnification)

---

**ข้อ 78:** ใน mammography, compression ช่วยในเรื่องใดบ้าง?
- A. ลด thickness → ลด scatter และ dose
- B. แยก tissue overlapping
- C. ลด motion artifact
- D. ทั้ง A, B, C

**เฉลย: D** — Compression มีประโยชน์หลายอย่าง: ลด scatter, ลด dose, แยก tissue, ลด motion

---

**ข้อ 79:** Spot-compression mammography ใช้เมื่อใด?
- A. Routine screening
- B. Characterize lesion ที่ไม่แน่ใจจากมาตรฐาน
- C. ทดแทน MLO
- D. ตรวจ calcification ขนาดใหญ่

**เฉลย: B** — Spot compression = additional view → บีบเฉพาะบริเวณ lesion → ดู lesion ชัดขึ้น, แยก summation shadow

---

**ข้อ 80:** ระยะ organogenesis ของทารกที่เสี่ยง congenital malformation จากรังสีมากที่สุดคือ
- A. สัปดาห์ที่ 0-2
- B. สัปดาห์ที่ 2-8
- C. สัปดาห์ที่ 8-15
- D. สัปดาห์ที่ 16-40

**เฉลย: B** — Organogenesis = สัปดาห์ 2-8 → เสี่ยง congenital malformation, threshold ~50-100 mGy

---

## หมวด C: CT, MRI, Nuclear Medicine, Contrast (ข้อ 81-120)

**ข้อ 81:** ใน CT, beam hardening artifact พบบ่อยที่ตำแหน่งใด?
- A. Lung
- B. ระหว่าง petrous bone ทั้งสองด้าน (posterior fossa)
- C. Subcutaneous fat
- D. อากาศใน bowel

**เฉลย: B** — Beam hardening streak ที่ posterior fossa (ระหว่าง petrous bone) เป็น artifact ที่พบบ่อยใน CT brain

---

**ข้อ 82:** Ring artifact ใน CT เกิดจาก
- A. Metal implant
- B. Patient movement
- C. Detector channel ที่ calibration ผิดพลาดหรือเสีย
- D. kVp ไม่เหมาะสม

**เฉลย: C** — Ring artifact = detector channel ที่อ่าน signal ผิดพลาด → วงกลม concentric บน image

---

**ข้อ 83:** MRI safety: implant ใดที่ถือว่า "MR Unsafe" โดยทั่วไป?
- A. IUD (Copper)
- B. Hip prosthesis (titanium)
- C. Conventional cardiac pacemaker
- D. Dental implant

**เฉลย: C** — Conventional pacemaker = **MR Unsafe** (ferromagnetic component + electromagnetic interference กับ pacemaker programming)

---

**ข้อ 84:** Gadolinium MRI contrast ห้ามใช้ในผู้ป่วย renal failure เพราะ
- A. Nephrotoxicity โดยตรง
- B. NSF (Nephrogenic Systemic Fibrosis) โดยเฉพาะ linear Gd
- C. Allergic reaction รุนแรง
- D. ทำให้ HU เปลี่ยน

**เฉลย: B** — NSF เป็น progressive fibrosis ของ skin และอวัยวะ พบใน eGFR < 30 ที่ฉีด linear Gd

---

**ข้อ 85:** Tc-99m มี physical half-life เท่าใด?
- A. 2 ชั่วโมง
- B. 6 ชั่วโมง
- C. 13 ชั่วโมง
- D. 8 วัน

**เฉลย: B** — Tc-99m T½ = **6.02 ชั่วโมง** (เหมาะสำหรับ nuclear medicine scanning)

---

**ข้อ 86:** PET scan ใช้หลักการ coincidence detection ของ photon พลังงาน
- A. 140 keV
- B. 364 keV
- C. 511 keV (annihilation photon)
- D. 1.02 MeV

**เฉลย: C** — β⁺ + e⁻ → annihilation → 2 photons **511 keV** ทิศตรงข้าม → coincidence detection

---

**ข้อ 87:** Collimator ชนิดใดเหมาะกับ I-131 (364 keV)?
- A. LEHR (Low Energy High Resolution)
- B. MEGP (Medium Energy)
- C. HEGP (High Energy)
- D. Pinhole

**เฉลย: C** — I-131 มีพลังงานสูง (364 keV) → ต้องใช้ **HEGP** collimator ที่มี lead หนาพอ

---

**ข้อ 88:** Radionuclide ใดที่ใช้ใน bone scan มากที่สุด?
- A. I-131
- B. Ga-67
- C. Tc-99m MDP
- D. F-18 FDG

**เฉลย: C** — Bone scan มาตรฐาน = **Tc-99m MDP** (Methylene Diphosphonate)

---

**ข้อ 89:** Contrast reaction severe (anaphylaxis) — ยาแรกที่ต้องให้ทันทีคือ
- A. Diphenhydramine IV
- B. Hydrocortisone IV
- C. Epinephrine 0.5 mg IM (1:1000)
- D. Normal saline bolus

**เฉลย: C** — **Epinephrine** คือยาหลักสำหรับ anaphylaxis → IM ที่ lateral thigh → เร็วที่สุด

---

**ข้อ 90:** Barium ห้ามใช้เมื่อสงสัยภาวะใด?
- A. Dysphagia
- B. Peptic ulcer
- C. Perforation (suspected GI perforation)
- D. Constipation

**เฉลย: C** — Barium + perforation → **Barium peritonitis** → ร้ายแรงถึงชีวิต → ใช้ water-soluble contrast แทน

---

**ข้อ 91:** ปัจจัยใดที่เพิ่มความเสี่ยง Contrast-Induced Nephropathy (CIN) มากที่สุด?
- A. Age > 60
- B. Pre-existing renal insufficiency
- C. Hypertension
- D. การใช้ LOCM

**เฉลย: B** — **Pre-existing renal insufficiency** เป็น risk factor หลักที่สุดของ CIN

---

**ข้อ 92:** MRI wrap-around (aliasing) artifact เกิดเพราะ
- A. Patient movement
- B. FOV เล็กกว่าขนาด patient → signal นอก FOV overlap เข้ามา
- C. TE ยาวเกินไป
- D. Metal implant

**เฉลย: B** — Aliasing/wrap-around: anatomy ที่อยู่นอก FOV "wrap" ไปปรากฏอีกด้านของภาพ

---

**ข้อ 93:** CT coronary angiography ต้องการ temporal resolution สูง → ใช้เทคโนโลยีใด?
- A. Single-slice CT
- B. Multi-detector CT (MDCT) 64-slice ขึ้นไป + ECG gating
- C. Sequential scanning
- D. Standard helical CT

**เฉลย: B** — Cardiac CT ต้องการ 64-slice ขึ้นไป + **ECG gating** (prospective หรือ retrospective) เพื่อ freeze cardiac motion

---

**ข้อ 94:** SPECT ต่างจาก Planar scintigraphy อย่างไร?
- A. SPECT ใช้ radiopharmaceutical ต่างกัน
- B. SPECT camera หมุนรอบผู้ป่วย → ได้ 3D tomographic image
- C. SPECT ใช้ X-ray แทน gamma
- D. SPECT ไม่ต้องการ collimator

**เฉลย: B** — SPECT: camera หมุนเก็บ multiple projections → reconstruction → 3D image

---

**ข้อ 95:** Myelography ต้องใช้ contrast ชนิดใด?
- A. Barium sulfate
- B. High osmolar iodinated contrast (HOCM)
- C. Non-ionic, low/iso-osmolar water-soluble contrast
- D. Gadolinium

**เฉลย: C** — Myelography = intrathecal injection → ต้องใช้ **non-ionic, water-soluble** (เช่น Iohexol/Omnipaque) เท่านั้น

---

**ข้อ 96:** DWI bright + ADC dark ใน MRI หมายถึง
- A. T2 shine-through
- B. Restricted diffusion (ischemia, abscess)
- C. Free diffusion
- D. Hemorrhage เก่า

**เฉลย: B** — DWI bright + ADC dark = **true restricted diffusion** (ischemia, abscess, hypercellular tumor)

---

**ข้อ 97:** V/Q scan ใช้ตรวจอะไร?
- A. Cardiac output
- B. Pulmonary embolism
- C. Liver function
- D. Renal perfusion

**เฉลย: B** — V/Q scan (Ventilation/Perfusion) = ตรวจ **Pulmonary Embolism** → mismatch (normal V + abnormal Q)

---

**ข้อ 98:** Metformin ต้องหยุดก่อนและหลังฉีด iodinated contrast กี่ชั่วโมง?
- A. 12 ชั่วโมง
- B. 24 ชั่วโมง
- C. 48 ชั่วโมง
- D. 72 ชั่วโมง

**เฉลย: C** — Metformin: หยุด **48 ชั่วโมง** ก่อนฉีด (ถ้า renal function ไม่ดี) และ 48 ชั่วโมงหลัง จนเช็ค creatinine ได้แล้ว

---

**ข้อ 99:** HVL ใน CT บ่งบอกถึงอะไร?
- A. ขนาดของ focal spot
- B. Beam quality ของ X-ray
- C. ขนาด pixel
- D. ความเร็ว rotation

**เฉลย: B** — HVL = beam quality indicator → CT มี kVp สูง (80-140 kVp) → HVL สูง

---

**ข้อ 100:** ผู้ป่วย eGFR = 25 mL/min/1.73m² ต้องการ CT contrast — ควรทำอย่างไร?
- A. ฉีด HOCM ตามปกติ
- B. ฉีด LOCM ครึ่ง dose
- C. ปรึกษาแพทย์ พิจารณาไม่ฉีด / ใช้ MRI แทน / ถ้าจำเป็นใช้ IOCM + hydration เต็มที่
- D. ฉีดได้ทันทีเพราะ LOCM ปลอดภัย

**เฉลย: C** — eGFR < 30 → high risk CIN → ต้องปรึกษา พิจารณาทางเลือกอื่น หรือ hydration + IOCM อย่างระมัดระวัง

---

## หมวด D: QC, Safety, Law (ข้อ 101-130)

**ข้อ 101:** Reject rate ที่ยอมรับได้ในแผนก general radiography คือ
- A. <1%
- B. <4-8%
- C. <20%
- D. ไม่มีขีดจำกัด

**เฉลย: B** — Reject rate ยอมรับได้ ≤ **4-8%** (ส่วนใหญ่ target ≤5%)

---

**ข้อ 102:** Mammography phantom test: ต้องเห็น fibers อย่างน้อยกี่เส้น?
- A. 2 fibers
- B. 4 fibers
- C. 6 fibers
- D. 8 fibers

**เฉลย: B** — ACR mammography phantom: ≥**4 fibers**, ≥3 specks, ≥3 masses

---

**ข้อ 103:** Personal dosimeter ชนิดใดที่อ่านค่าได้ real-time?
- A. TLD
- B. OSL
- C. Film badge
- D. Pocket ionization chamber

**เฉลย: D** — Pocket dosimeter (ionization chamber) อ่านได้ทันที แต่ TLD, OSL, Film badge ต้องส่งแล็บ

---

**ข้อ 104:** kVp accuracy tolerance ที่ยอมรับได้ใน QC คือ
- A. ±1%
- B. ±5%
- C. ±10%
- D. ±15%

**เฉลย: B** — kVp accuracy ≤ **±5%** ของค่าตั้ง

---

**ข้อ 105:** Dose limit สำหรับประชาชนทั่วไปต่อปีคือ
- A. 1 mSv
- B. 5 mSv
- C. 20 mSv
- D. 50 mSv

**เฉลย: A** — General public: **1 mSv/year**

---

**ข้อ 106:** Fluoroscopy: air kerma ถึงเท่าใดที่ต้องแจ้งเตือนเรื่อง skin injury?
- A. 1 Gy
- B. 3 Gy
- C. 10 Gy
- D. 50 Gy

**เฉลย: B** — Air kerma ≥ **3 Gy** → threshold สำหรับ notification/documentation เรื่อง radiation-induced skin injury

---

**ข้อ 107:** มาตรการใดลด patient dose ใน fluoroscopy ได้มากที่สุด?
- A. เพิ่ม kVp
- B. Pulsed fluoroscopy
- C. เพิ่ม SID
- D. ใส่ lead apron ให้ผู้ป่วย

**เฉลย: B** — **Pulsed fluoroscopy** ลด dose ได้ 50-75% เทียบ continuous

---

**ข้อ 108:** ใบอนุญาตวิชาชีพรังสีเทคนิคมีอายุกี่ปี?
- A. 1 ปี
- B. 3 ปี
- C. 5 ปี
- D. 10 ปี

**เฉลย: C** — ใบอนุญาตประกอบวิชาชีพรังสีเทคนิค มีอายุ **5 ปี**

---

**ข้อ 109:** หลัก ALARA ย่อมาจาก
- A. As Long As Radiation Allows
- B. As Low As Reasonably Achievable
- C. All Limits Applied Radiation Annually
- D. As Low As Radiation Applies

**เฉลย: B** — ALARA = **As Low As Reasonably Achievable**

---

**ข้อ 110:** Total filtration ขั้นต่ำสำหรับหลอด X-ray ที่ใช้ทางการแพทย์คือ
- A. 1.0 mm Al
- B. 1.5 mm Al
- C. 2.5 mm Al
- D. 5.0 mm Al

**เฉลย: C** — Total filtration (inherent + added) ≥ **2.5 mm Al equivalent** (กฎหมาย/มาตรฐาน)

---

**ข้อ 111:** การ Hand hygiene ที่ถูกต้องตาม WHO 5 Moments ต้องล้างมือเมื่อใด?
- A. ก่อนสัมผัสผู้ป่วยเท่านั้น
- B. หลังสัมผัสผู้ป่วยเท่านั้น
- C. ก่อนสัมผัส, ก่อนทำ aseptic procedure, หลังสัมผัส body fluid, หลังสัมผัสผู้ป่วย, หลังสัมผัสสิ่งแวดล้อมรอบผู้ป่วย
- D. เฉพาะก่อนหัตถการ

**เฉลย: C** — WHO 5 Moments: before patient contact, before aseptic, after body fluid, after patient, after patient surroundings

---

**ข้อ 112:** ผู้ป่วย TB ต้องใช้ PPE ชนิดใดในห้อง X-ray?
- A. Surgical mask
- B. N95 respirator
- C. ถุงมือเท่านั้น
- D. ไม่ต้องใช้ PPE พิเศษ

**เฉลย: B** — TB = airborne transmission → ต้องใช้ **N95 respirator** (ไม่ใช่ surgical mask)

---

**ข้อ 113:** Informed consent องค์ประกอบใดที่สำคัญที่สุด?
- A. ลายเซ็นผู้ป่วย
- B. ผู้ป่วยเข้าใจข้อมูลและตัดสินใจเอง (Voluntariness + Comprehension)
- C. แพทย์เซ็น
- D. มีพยาน 2 คน

**เฉลย: B** — Consent ที่แท้จริงต้องการ: ผู้ป่วยได้รับข้อมูล + เข้าใจ + ตัดสินใจเองโดยไม่ถูกบังคับ

---

**ข้อ 114:** DICOM คือ
- A. ระบบ billing ของแผนกรังสี
- B. มาตรฐาน format สำหรับ medical images และการสื่อสารข้อมูล
- C. ซอฟต์แวร์สำหรับ CT reconstruction
- D. Protocol การฉีด contrast

**เฉลย: B** — DICOM = Digital Imaging and Communications in Medicine → มาตรฐาน interoperability ของ medical imaging

---

**ข้อ 115:** Stochastic effect ที่สำคัญที่สุดของรังสีในประชากรทั่วไปคือ
- A. Radiation-induced cataract
- B. Radiation-induced cancer / leukemia
- C. Skin erythema
- D. Hair loss

**เฉลย: B** — Stochastic = cancer induction (somatic) และ genetic mutation (hereditary) — ไม่มี threshold

---

**ข้อ 116:** สาเหตุ reject ที่พบบ่อยที่สุดใน general radiography คือ
- A. Exposure error
- B. Positioning error
- C. Motion artifact
- D. Equipment failure

**เฉลย: B** — **Positioning error** มักเป็นสาเหตุ reject อันดับ 1 (~30%)

---

**ข้อ 117:** Lead apron (0.5 mm Pb) ลด scatter radiation ได้ประมาณ
- A. 25%
- B. 50%
- C. 75%
- D. 95%

**เฉลย: D** — Lead apron 0.5 mm Pb ลด scatter ได้ ~**95%** ที่ diagnostic energy ranges

---

**ข้อ 118:** Dose creep ป้องกันได้ดีที่สุดด้วยวิธีใด?
- A. เพิ่ม kVp
- B. ติดตาม Exposure Index (EI) อย่างสม่ำเสมอ + reject analysis
- C. ลด FOV
- D. ใช้ grid ratio สูงขึ้น

**เฉลย: B** — การ monitor EI และ reject analysis เป็น tool หลักในการตรวจจับ dose creep

---

**ข้อ 119:** Standard Precaution ใช้กับผู้ป่วยกลุ่มใด?
- A. เฉพาะผู้ป่วยที่ known infectious disease
- B. ทุกผู้ป่วยโดยไม่คำนึงถึงการวินิจฉัย
- C. เฉพาะ ICU patients
- D. เฉพาะ HIV/AIDS

**เฉลย: B** — Standard Precautions ใช้กับ **ทุกผู้ป่วย** ทุกการสัมผัส (ถือว่า blood, body fluid ทุกราย potentially infectious)

---

**ข้อ 120:** สภาวิชาชีพรังสีเทคนิคมีหน้าที่อะไร?
- A. ฝึกอบรมนักรังสีเทคนิค
- B. ออกและต่ออายุใบอนุญาตประกอบวิชาชีพ
- C. จัดซื้อครุภัณฑ์รังสี
- D. กำหนดขีดจำกัดปริมาณรังสี

**เฉลย: B** — สภาวิชาชีพรังสีเทคนิค: ออก/ต่ออายุใบอนุญาต, กำกับจรรยาบรรณ, กำหนด CPD requirements

---

## หมวด E: Clinical Correlation & Integration (ข้อ 121-150)

**ข้อ 121:** ผู้ป่วย stroke acute onset 2 ชั่วโมง — การตรวจ imaging ลำดับแรกคือ
- A. MRI brain ทันที
- B. Non-contrast CT brain ทันที
- C. CT angiography
- D. Carotid Doppler

**เฉลย: B** — Non-contrast CT brain **ก่อนเสมอ** เพื่อ rule out hemorrhage (ถ้า bleed → ห้าม thrombolysis)

---

**ข้อ 122:** ผู้ป่วย trauma abdominal ที่ hemodynamically stable — imaging ที่ดีที่สุดคือ
- A. Abdominal X-ray
- B. Ultrasound (FAST exam)
- C. CT abdomen with IV contrast
- D. MRI abdomen

**เฉลย: C** — CT abdomen + pelvis with IV contrast = **gold standard** สำหรับ abdominal trauma (stable)

---

**ข้อ 123:** ผู้ป่วย suspected pulmonary embolism ที่ไม่ได้ตั้งครรภ์ — imaging ที่ดีที่สุดคือ
- A. Chest X-ray
- B. V/Q scan
- C. CT pulmonary angiography (CTPA)
- D. MRI chest

**เฉลย: C** — **CTPA** คือ gold standard สำหรับ PE (เร็ว, accurate) — V/Q scan ใช้เมื่อ CI ต่อ contrast หรือตั้งครรภ์

---

**ข้อ 124:** ผู้ป่วยสงสัย appendicitis — imaging ลำดับแรกในผู้ใหญ่คือ
- A. Abdominal X-ray
- B. CT abdomen/pelvis with contrast
- C. Ultrasound (ก่อน)
- D. MRI

**เฉลย: C** — Ultrasound ก่อน (ไม่มี radiation, ราคาถูก) แต่ถ้าไม่ conclusive → CT abdomen/pelvis

---

**ข้อ 125:** ผู้ป่วย known pacemaker (MR Unsafe) ต้องการตรวจ lumbar spine — ทำอะไรแทน MRI?
- A. CT myelogram
- B. Plain X-ray เท่านั้น
- C. PET scan
- D. ไม่มีทางเลือกอื่น

**เฉลย: A** — CT myelogram (CT + intrathecal contrast) = ทางเลือกที่ดีเมื่อ MRI CI

---

**ข้อ 126:** Hyperdense MCA sign ใน CT brain หมายถึง
- A. Old hemorrhage
- B. Acute clot ใน middle cerebral artery → acute ischemic stroke
- C. Tumor
- D. Normal variant

**เฉลย: B** — Hyperdense MCA sign = fresh thrombus (clot) ใน MCA → acute ischemic stroke

---

**ข้อ 127:** ผู้ป่วย 35 สัปดาห์ตั้งครรภ์ สงสัย appendicitis — imaging ที่เหมาะสมที่สุดคือ
- A. CT abdomen ก่อน
- B. Ultrasound → ถ้าไม่ conclusive → MRI (ไม่ใช้ Gadolinium)
- C. Plain X-ray ก่อน
- D. ไม่ทำ imaging ใดๆ

**เฉลย: B** — หญิงตั้งครรภ์: Ultrasound ก่อน → MRI (ไม่มี radiation) ถ้า US ไม่ชัด → CT เป็นทางเลือกสุดท้าย

---

**ข้อ 128:** ผู้ป่วย hemoptysis สงสัย bronchogenic carcinoma — imaging ที่ดีที่สุดคือ
- A. Chest X-ray เท่านั้น
- B. CT chest with contrast
- C. MRI chest
- D. Bronchoscopy เท่านั้น

**เฉลย: B** — CT chest with IV contrast = best for lung cancer staging, mediastinum, vascular involvement

---

**ข้อ 129:** Anaphylaxis จาก contrast media — หลังให้ Epinephrine แล้วยังไม่ดีขึ้น — ต้องทำอะไรต่อ?
- A. เพิ่ม Epinephrine dose ซ้ำ
- B. IV fluid (saline) + O₂ + ขอ emergency team / activate code
- C. ให้ Antihistamine เท่านั้น
- D. รอดูอาการ

**เฉลย: B** — ถ้า Epinephrine แล้วไม่ดีขึ้น → ซ้ำ Epi + IV fluid + O₂ + **CPR/ACLS** ถ้าจำเป็น + ขอ emergency team

---

**ข้อ 130:** ผู้ป่วย claustrophobia ต้องการ MRI brain — วิธีจัดการที่เหมาะสมคือ
- A. บังคับให้ทำ
- B. ยกเลิกการตรวจ CT แทนทุกกรณี
- C. อธิบาย, ให้ anxiolytic ถ้าจำเป็น, ใช้ open MRI หรือ short-bore magnet
- D. ไม่มีทางเลือกอื่น

**เฉลย: C** — Claustrophobia: อธิบาย procedure, ใช้ anxiolytic/sedation ถ้าจำเป็น, open MRI หรือ short-bore ช่วยได้

---

**ข้อ 131-150: ข้อสอบ Advanced Integration**

**ข้อ 131:** ผู้ป่วยสูงอายุ osteoporotic กระดูกสะโพกหัก — ไม่ชัดใน X-ray — imaging ต่อไปคือ
- A. CT สะโพก
- B. MRI สะโพก (most sensitive for occult hip fracture)
- C. Bone scan
- D. Repeat X-ray ใน 2 สัปดาห์

**เฉลย: B** — MRI คือ **gold standard** สำหรับ occult hip fracture — sensitive ที่สุด (เร็ว, ไม่มี radiation)

---

**ข้อ 132:** ใน MRI, magic angle artifact พบที่โครงสร้างใด?
- A. Brain white matter
- B. Tendon ที่เอียง 55° กับ B₀ (เช่น rotator cuff, Achilles)
- C. Joint effusion
- D. Fatty tumor

**เฉลย: B** — Magic angle effect: tendon เอียง **55°** กับ B₀ → bright ใน short TE → false positive for tendinopathy

---

**ข้อ 133:** Iterative reconstruction ใน CT ดีกว่า Filtered Back Projection (FBP) อย่างไร?
- A. เร็วกว่า FBP
- B. ลด noise ที่ mAs ต่ำได้ → ลด patient dose
- C. ไม่มี artifact
- D. ใช้ได้กับเครื่อง CT รุ่นเก่า

**เฉลย: B** — Iterative reconstruction → ลด image noise ที่ mAs ต่ำ → สามารถลด dose โดยยัง maintain image quality

---

**ข้อ 134:** ผู้ป่วย claustrophobia รุนแรงและต้องการตรวจ MSK (knee) — ทางเลือกคือ
- A. CT knee
- B. Ultrasound
- C. Open MRI หรือ peripheral MRI
- D. ไม่ตรวจ

**เฉลย: C** — Open MRI หรือ extremity/peripheral MRI ลด claustrophobia → ทางเลือกสำหรับ extremity imaging

---

**ข้อ 135:** ใน Nuclear Medicine, "Hot spot" บน bone scan หมายถึง
- A. บริเวณที่มี decreased uptake
- B. บริเวณที่มี increased uptake (osteoblastic activity)
- C. Artifact
- D. Normal cortex

**เฉลย: B** — Hot spot = increased Tc-99m MDP uptake → osteoblastic activity (fracture, metastasis, infection)

---

**ข้อ 136:** Portal venous phase CT abdomen ถ่ายที่เวลาใด?
- A. 20-30 วินาที
- B. 60-70 วินาที
- C. 3-5 นาที
- D. 10-15 นาที

**เฉลย: B** — Portal venous phase = **60-70 วินาที** หลัง contrast → liver parenchyma enhancement สูงสุด

---

**ข้อ 137:** GTV ใน radiation therapy planning คืออะไร?
- A. CTV + margin สำหรับ setup error
- B. ก้อนมะเร็งที่มองเห็นได้ใน imaging (Gross Tumor Volume)
- C. Organ ที่ต้องป้องกัน
- D. บริเวณ microscopic extension

**เฉลย: B** — GTV = Gross Tumor Volume = ก้อนที่เห็นชัดใน imaging/clinical exam

---

**ข้อ 138:** HDR brachytherapy มี dose rate สูงกว่า
- A. 0.4-2 Gy/hr
- B. 2-12 Gy/hr
- C. >12 Gy/hr
- D. ขึ้นกับ source

**เฉลย: C** — HDR (High Dose Rate) = **>12 Gy/hr** (LDR = 0.4-2 Gy/hr)

---

**ข้อ 139:** ใน CT, automatic tube current modulation (ATCM) ทำงานอย่างไร?
- A. ปรับ kVp ตามขนาดผู้ป่วย
- B. ปรับ mA ตาม patient thickness/attenuation → ลด dose ส่วน thin regions
- C. ปรับ slice thickness
- D. ปรับ pitch

**เฉลย: B** — ATCM/AEC ใน CT ปรับ mA ตาม attenuation (ลด mA ที่บริเวณบาง → ลด dose รวม)

---

**ข้อ 140:** ใน mammography, calcification แบบใดที่ suspicious สำหรับ malignancy ที่สุด?
- A. Coarse/popcorn
- B. Vascular (train-track)
- C. Fine linear/branching
- D. Milk of calcium

**เฉลย: C** — Fine linear/branching calcification = **DCIS pattern** → highly suspicious

---

**ข้อ 141:** ผู้ป่วยอุบัติเหตุ — suspected C-spine injury — X-ray lateral ไม่เห็น C7-T1 junction — ควรทำอะไร?
- A. หยุดตรวจ
- B. Swimmer's view (Twining method)
- C. PA C-spine
- D. Odontoid view

**เฉลย: B** — Swimmer's view = ทางเลือกเมื่อ lateral C-spine ไม่เห็น **C7-T1** junction เนื่องจาก shoulder

---

**ข้อ 142:** ใน fluoroscopy, Last Image Hold (LIH) ประโยชน์หลักคือ
- A. เพิ่ม image quality
- B. ลด patient dose โดยดู image โดยไม่ต้อง activate beam ใหม่
- C. เพิ่ม frame rate
- D. ลด scatter

**เฉลย: B** — LIH = hold last acquired frame → ดูได้โดยไม่ต้องเปิด X-ray ใหม่ → ลด patient dose

---

**ข้อ 143:** Radiation weighting factor (Wr) ของ alpha particle คือ
- A. 1
- B. 5
- C. 10
- D. 20

**เฉลย: D** — Alpha particle Wr = **20** (high LET radiation → biological damage สูง)

---

**ข้อ 144:** Fringe field ของ MRI magnet อันตรายอย่างไร?
- A. ทำให้ผู้ป่วยร้อน
- B. Ferromagnetic object ถูกดูดแม้อยู่นอกห้อง → projectile effect
- C. Interfere กับ X-ray machine ข้างเคียง
- D. ทำให้ patient nausea

**เฉลย: B** — Fringe field ยาวออกมานอกห้อง → metal objects ถูกดูดเข้าหา magnet → projectile อันตราย

---

**ข้อ 145:** ใน SPECT myocardial perfusion imaging — Stress/rest mismatch (defect ที่ stress แต่ normal ที่ rest) หมายถึง
- A. Myocardial infarction (scar)
- B. Ischemia (reversible perfusion defect)
- C. Artifact
- D. Normal

**เฉลย: B** — Stress defect + Rest normal = **reversible** → ischemia (viable myocardium ที่ขาดเลือดตอน stress แต่ recover ที่ rest)

---

**ข้อ 146:** ผู้ป่วย renal cell carcinoma staging — imaging ที่ดีที่สุดคือ
- A. IVP
- B. Ultrasound
- C. CT abdomen/pelvis + CT chest with contrast
- D. MRI ท้องเท่านั้น

**เฉลย: C** — RCC staging: CT abdomen/pelvis (primary + LN + vascular) + CT chest (lung mets) คือมาตรฐาน

---

**ข้อ 147:** ข้อใดถูกต้องเกี่ยวกับ DICOM?
- A. Format เฉพาะ CT
- B. ต้องใช้ internet
- C. Header ประกอบด้วย patient demographics, acquisition parameters, study info
- D. ใช้ได้เฉพาะใน PACS

**เฉลย: C** — DICOM header บรรจุข้อมูลสมบูรณ์: patient ID, modality, scan parameters, institution ฯลฯ

---

**ข้อ 148:** ผู้ป่วย suspected DVT ขาข้างซ้าย — imaging ที่ดีที่สุดคือ
- A. Venography (contrast)
- B. Compression ultrasound (Duplex)
- C. MRI venography
- D. CT venography

**เฉลย: B** — **Compression ultrasound (Duplex)** = first-line, non-invasive, accurate สำหรับ DVT

---

**ข้อ 149:** ใน radiation therapy, 4 R ข้อใดอธิบายว่าทำไม fractionation ดีกว่า single dose?
- A. Repair — เซลล์ปกติซ่อมแซมได้ดีกว่ามะเร็ง + Repopulation เซลล์ปกติ
- B. Redistribution เซลล์มะเร็งในเฟส resistant
- C. Reoxygenation ทำให้ hypoxic tumor sensitive ขึ้น
- D. ทั้ง A, B, C (ทุกข้อรวมกัน)

**เฉลย: D** — Fractionation ดีกว่า single dose เพราะ 4R ทั้งหมดทำงานร่วมกัน

---

**ข้อ 150:** ผู้ป่วยได้รับ Gadolinium และ 2 วันต่อมา creatinine เพิ่มขึ้น 0.3 mg/dL จาก baseline — ควรพิจารณาอะไร?
- A. ผลปกติ Gadolinium ไม่ nephrotoxic
- B. NSF — ต้องรักษาทันที
- C. สังเกตอาการ ตรวจ renal function ซ้ำ พิจารณา CIN from concurrent iodinated contrast (ถ้ามี)
- D. Gadolinium allergy

**เฉลย: C** — Gadolinium เองไม่ nephrotoxic โดยตรงเหมือน iodinated contrast แต่ต้องสังเกต trend creatinine และดูว่ามี concurrent iodinated contrast ด้วยหรือเปล่า; NSF ต้องใช้เวลานานกว่า (สัปดาห์-เดือน)

---

# 🚀 SECTION 18 — CRASH COURSE BEFORE EXAM

## 18.1 Timeline 24 ชั่วโมงก่อนสอบ

### 24 ชั่วโมงก่อนสอบ (วันก่อน)
**ตอนเช้า (08:00-12:00):**
- ทบทวน Physics สูตรสำคัญ
- ทบทวน Contrast reaction management
- ทบทวน Dose limits

**ตอนบ่าย (13:00-17:00):**
- ทบทวน Positioning (chest, skull, spine)
- ทบทวน CT windows
- ทบทวน MRI T1/T2 signals

**ตอนเย็น (17:00-20:00):**
- ทบทวน Nuclear Medicine (Tc-99m, PET)
- ทบทวน QC criteria
- ทบทวน Law/Ethics

**ก่อนนอน (20:00-22:00):**
- อ่าน High-yield summary
- ทบทวน Mnemonics ทั้งหมด
- หยุดอ่าน — พักผ่อน

### วันสอบ (เช้า)
- ตื่นนอนพอดี — อย่าตื่นเร็วจนเครียด
- กินอาหารเบาๆ (อย่าให้หิวหรือง่วง)
- ทบทวน mnemonic 30 นาที
- นำบัตร identity + เอกสารครบ

## 18.2 เรื่องที่ต้องท่องก่อนสอบ

### Physics
```
✅ Inverse square law: I ∝ 1/D²
✅ mAs compensation: mAs₂ = mAs₁ × (SID₂/SID₁)²
✅ 15% kVp rule: +15% kVp = ×2 mAs
✅ Magnification: MF = SID/SOD
✅ Dose limits: Occupational = 20 mSv/yr, Public = 1 mSv/yr, Pregnant = 1 mSv
✅ HVL formula: I = I₀ × (½)^(x/HVL)
✅ Larmor: ω₀ = γ × B₀ = 42.58 MHz/T
✅ HU: Water=0, Air=-1000, Fat=-80-120, Blood=50-90, Bone>400
```

### Positioning
```
✅ PA chest SID = 180 cm
✅ Waters = Maxillary sinus (15° cephalad, acanthion ชิด IR)
✅ Caldwell = Frontal/Ethmoid (PA 15° caudal)
✅ Towne = Occipital (AP 30° caudal)
✅ Scottie dog: Neck = Pars interarticularis, Collar = Spondylolysis
✅ Swimmer's view = C7-T1 junction
✅ Decubitus: Left lateral = ดู right pleural fluid
✅ MLO mammography: pectoralis ถึง nipple level
```

### MRI/CT
```
✅ T1: Fat=bright, Water=dark
✅ T2: Fat=intermediate, Water=bright, CSF=bright
✅ FLAIR: CSF suppressed (dark)
✅ DWI bright + ADC dark = restricted diffusion = acute stroke/abscess
✅ CT brain window: WW=80, WL=40
✅ CT lung window: WW=1500, WL=-600
✅ Gadolinium NSF: macrocyclic safer than linear
✅ MRI zones: I-II-III-IV (Zone IV = magnet room)
```

### Contrast
```
✅ Epinephrine severe reaction: 0.5 mg IM (1:1000)
✅ Barium + perforation = CONTRAINDICATED
✅ CIN prevention: hydration, LOCM/IOCM, avoid Metformin
✅ Metformin: หยุด 48 ชั่วโมง ถ้า renal ไม่ดี
✅ Gadolinium NSF: eGFR <30 → ระวัง/ห้าม linear Gd
```

### Nuclear Medicine
```
✅ Tc-99m: T½ = 6 hr, 140 keV, used in bone scan, cardiac, thyroid
✅ F-18 FDG: PET, β⁺, 511 keV annihilation, glucose metabolism
✅ I-131: T½ = 8 days, thyroid treatment
✅ LEHR = Tc-99m, HEGP = I-131
✅ Bone scan hot spot = increased osteoblastic activity
```

## 18.3 เรื่องที่ควรปล่อย (ถ้าเวลาน้อย)

- รายละเอียด generator factor ทุก type
- Crystallography ของ TLD material
- LINAC electron gun mechanism ลึกๆ
- Brachytherapy isodose curve calculation
- MRI k-space mathematics
- Exact chemical formula ของ radiopharmaceutical ทุกตัว

## 18.4 เทคนิคทำข้อสอบ

### การอ่านโจทย์
1. **อ่าน stem ช้าๆ** — มองหา key words: "most likely," "best," "first," "contraindicated"
2. **อ่านตัวเลือกก่อนกลับไปอ่าน stem** — บางครั้งช่วยโฟกัสได้
3. **ขีดเส้นใต้** keyword สำคัญ

### การตัดตัวเลือก
| เทคนิค | คำอธิบาย |
|-------|---------|
| **Extreme เกินไป** | "always," "never," "only" มักผิด |
| **Too specific** | ถ้ามีคำตอบที่ครอบคลุมกว่า มักถูก |
| **ตัดคู่** | ถ้ามี 2 ตัวเลือกที่ตรงข้ามกัน คำตอบมักอยู่ใน 2 นั้น |
| **Longest answer** | บางครั้ง longest = most complete = correct |
| **"All of the above"** | มักถูกถ้าตัวเลือกอื่นถูกหมด |

### เมื่อไม่แน่ใจ
- **Eliminate** ตัวเลือกที่ผิดชัดเจนก่อน
- **Trust first instinct** — อย่าเปลี่ยนบ่อย
- **ไม่มีคะแนนติดลบ** (ถ้าไม่มีกฎบอก) → ตอบทุกข้อ

## 18.5 เทคนิคบริหารเวลา

- ตรวจสอบจำนวนข้อและเวลา → คำนวณ **วินาทีต่อข้อ**
  - 200 ข้อ 3 ชั่วโมง = 180 min / 200 = **0.9 min/ข้อ**
- ข้อสั้น ทำเร็ว, ข้อยาวให้เวลามากกว่า
- **ทำรอบแรก** ข้อที่มั่นใจก่อน → **Mark** ข้อที่ไม่มั่นใจ
- รอบสอง: กลับมาทำข้อที่ mark ไว้

## 18.6 วิธีจำสูตรเร็ว (ก่อนสอบ 10 นาที)

**Inverse Square Law — "ระยะ 2 เท่า dose 4 เท่าน้อยลง"**

**15% kVp Rule — "เพิ่ม kVp 15% = mAs ×2"**

**HVL — "ผ่าน 1 HVL → เหลือ 50%, ผ่าน 3 HVL → เหลือ 12.5%, ผ่าน 10 HVL → เหลือ 0.1%"**

**Dose limits — "20-1-1" = Occupational 20 mSv, Public 1 mSv, Pregnant 1 mSv**

**MRI T1T2 — "FAT = T1, WATER = T2"**

**CT Windows — "Brain 80/40, Lung 1500/-600, Bone 4000/400"**

## 18.7 Mnemonic สุดท้าย — Master List

| Mnemonic | ความหมาย |
|---------|---------|
| **"TDS" (Three Dogs Shielding)** | Time, Distance, Shielding |
| **"FAT is T1, WATER is T2"** | MRI signal |
| **"Waters = น้ำ = Maxillary"** | Waters view |
| **"Towne = ท้ายทอย = Occipital"** | Towne view |
| **"Collar on Scottie dog = Spondylolysis"** | Oblique lumbar |
| **"20-1-1"** | Dose limits |
| **"Epi first in anaphylaxis"** | Contrast reaction |
| **"Barium + Perf = NO"** | Barium contraindication |
| **"Gd + Renal = NSF"** | Gadolinium safety |
| **"ALARA"** | As Low As Reasonably Achievable |
| **"Lymphocyte = Most radiosensitive"** | Radiosensitivity |
| **"DWI bright + ADC dark = Stroke"** | MRI stroke |
| **"PA Chest SID = 180"** | Chest positioning |
| **"Tc-99m = 6 hr, 140 keV"** | Nuclear medicine |
| **"Macrocyclic Gd = SAFE"** | MRI contrast |
| **"Pitch > 1 = gap = less dose"** | CT pitch |

## 18.8 สิ่งที่ห้ามพลาดในห้องสอบ

✅ **อ่านคำชี้แจงก่อนทุกครั้ง**
✅ **ตรวจสอบ answer sheet ให้ถูกข้อ**
✅ **ไม่ทิ้งข้อว่าง** (ถ้าไม่มี negative marking)
✅ **ใส่ชื่อ/เลขประจำตัว** ทุกหน้า
✅ **บริหารเวลา** — ดูนาฬิกาสม่ำเสมอ
✅ **ไม่เปลี่ยนคำตอบโดยไม่จำเป็น**
✅ **ทำรอบแรกให้จบก่อน** แล้วค่อย review

---

# 📊 APPENDIX — ตารางค่า Normal ที่ต้องรู้

## Physical Constants

| ค่า | ปริมาณ |
|-----|-------|
| Gyromagnetic ratio (H-1) | 42.58 MHz/T |
| Larmor frequency @ 1.5T | 63.87 MHz |
| Larmor frequency @ 3T | 127.74 MHz |
| K-shell binding energy (W) | 69.5 keV |
| Tc-99m energy | 140 keV |
| Annihilation photon (PET) | 511 keV |
| Pair production threshold | 1.02 MeV |
| LD50/30 (human) | 3-5 Gy |

## Dose Limits Summary

| กลุ่ม | Effective Dose |
|------|--------------|
| Occupational (whole body) | 20 mSv/yr |
| Occupational (skin/extremities) | 500 mSv/yr |
| Occupational (lens) | 20 mSv/yr |
| General public | 1 mSv/yr |
| Declared pregnant worker | 1 mSv (ตลอด pregnancy) |

## CT HU Values

| สาร | HU |
|----|----|
| Air | -1000 |
| Fat | -80 to -120 |
| Water | 0 |
| White matter | 20-30 |
| Gray matter | 35-45 |
| Acute blood | 50-90 |
| Muscle | 35-55 |
| Contrast (iodine) | 200-400+ |
| Bone (cortical) | 700-3000+ |

## MRI Sequences ย่อ

| T1 Short/Short | T2 Long/Long | PD Long/Short |
|---------------|--------------|--------------|
| Fat = bright | Water = bright | Proton density |
| Anatomy | Pathology | Cartilage, disc |
| Post-Gd | Edema, CSF | MSK imaging |

---

*คู่มือฉบับนี้ครอบคลุมทุก section ที่ออกสอบ — ขอให้โชคดีในการสอบ!*
*"Practice does not make perfect. Only perfect practice makes perfect." — Vince Lombardi*
