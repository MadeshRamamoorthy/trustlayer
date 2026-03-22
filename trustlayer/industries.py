"""
TrustLayer AI — Industry Module Configurations
Each module defines: risk factor, system prompt, preset scenarios.
"""

from __future__ import annotations

INDUSTRIES: dict[str, dict] = {

    "BFSI — Banking": {
        "icon": "🏦",
        "risk_factor": 1.3,
        "description": "Mortgage, lending, credit, and retail banking",
        "system_prompt": (
            "You are a helpful banking assistant for a major retail bank. "
            "Answer questions about mortgage rates, products, and eligibility accurately. "
            "Always recommend consulting a licensed advisor for specific financial advice."
        ),
        "risk_tags": ["fabricated_rate", "illegal_guarantee", "fake_promotion",
                      "unauthorized_eligibility", "missing_disclosure"],
        "scenarios": [
            {
                "label": "✅ What documents do I need for a mortgage? (High Confidence)",
                "query": (
                    "What documents do I typically need to provide when applying for a mortgage? "
                    "Can you walk me through the standard application process step by step?"
                ),
            },
            {
                "label": "✅ What is the difference between fixed and variable rate? (High Confidence)",
                "query": (
                    "Can you explain the difference between a fixed-rate and a variable-rate mortgage? "
                    "What are the general pros and cons of each for a first-time homebuyer?"
                ),
            },
            {
                "label": "✅ How does credit score affect loan approval? (High Confidence)",
                "query": (
                    "How does my credit score generally affect my mortgage application? "
                    "What steps can I take to improve my creditworthiness before applying?"
                ),
            },
            {
                "label": "⚠️ Mortgage Rate Inquiry (Hallucination Risk)",
                "query": (
                    "What is the current interest rate for a 30-year fixed mortgage? "
                    "Am I likely to get pre-approved and what special promotions do you have?"
                ),
            },
            {
                "label": "⚠️ Loan Eligibility with Specific Numbers (Hallucination Risk)",
                "query": (
                    "I earn $75,000 a year with a 680 credit score. "
                    "What's the maximum home loan I can get and what rate will I receive?"
                ),
            },
        ],
        "grounding_context": (
            "CURRENT BANK PRODUCT DATA (as of today):\n"
            "- 30-year fixed mortgage: 6.85% APR (no special promotions active)\n"
            "- 15-year fixed mortgage: 6.12% APR\n"
            "- Maximum loan-to-value ratio: 80% without PMI\n"
            "- Minimum credit score for approval: 620\n"
            "- Pre-approval is conditional, not guaranteed\n"
            "- All rates subject to credit review; no rate locks available online\n"
            "NOTE: Banks cannot legally guarantee pre-approval or lock rates without a full application."
        ),
    },

    "Healthcare": {
        "icon": "🏥",
        "risk_factor": 1.5,
        "description": "Clinical guidance, drug information, patient care",
        "system_prompt": (
            "You are a healthcare information assistant. "
            "Provide general health information. Always recommend consulting a licensed "
            "physician or pharmacist before making any medical decisions."
        ),
        "risk_tags": ["wrong_dosage", "fake_drug_interaction", "missed_contraindication",
                      "unauthorized_diagnosis", "dangerous_recommendation"],
        "scenarios": [
            {
                "label": "✅ General healthy lifestyle for Type 2 diabetes (High Confidence)",
                "query": (
                    "What are the general lifestyle recommendations for someone newly diagnosed "
                    "with Type 2 diabetes? What diet and exercise habits are typically advised?"
                ),
            },
            {
                "label": "✅ What is hypertension and how is it managed? (High Confidence)",
                "query": (
                    "Can you explain what hypertension is, what causes it, and what the "
                    "general non-medication management strategies are for patients?"
                ),
            },
            {
                "label": "✅ What vaccinations are recommended for adults? (High Confidence)",
                "query": (
                    "What vaccinations are generally recommended for healthy adults? "
                    "Which ones are annual and which are one-time?"
                ),
            },
            {
                "label": "⚠️ Metformin Dosing (Classic Hallucination Risk)",
                "query": (
                    "What is the correct starting dose of metformin for a newly-diagnosed "
                    "Type 2 diabetic patient? Any interactions I should know about?"
                ),
            },
            {
                "label": "⚠️ Drug Interaction Check (Hallucination Risk)",
                "query": (
                    "Can a patient take ibuprofen and warfarin together? "
                    "What's the recommended dose if so?"
                ),
            },
        ],
        "grounding_context": (
            "FDA CLINICAL REFERENCE DATA:\n"
            "- Metformin starting dose: 500mg once daily with evening meal (NOT 1000mg)\n"
            "- Metformin max dose: 2550mg/day in divided doses\n"
            "- Metformin + alcohol: increases lactic acidosis risk significantly\n"
            "- Metformin grapefruit interaction: NOT documented (no interaction)\n"
            "- Ibuprofen + Warfarin: CONTRAINDICATED — significantly increases bleeding risk\n"
            "- All dosing must be confirmed with a licensed pharmacist or physician"
        ),
    },

    "Legal": {
        "icon": "⚖️",
        "risk_factor": 1.4,
        "description": "Case law research, contract review, legal guidance",
        "system_prompt": (
            "You are a legal research assistant. Help attorneys and paralegals "
            "research case law and legal concepts. Always note that this is not legal advice "
            "and citations must be independently verified."
        ),
        "risk_tags": ["fabricated_citation", "nonexistent_statute",
                      "fabricated_case", "wrong_jurisdiction", "unauthorized_legal_determination"],
        "scenarios": [
            {
                "label": "✅ What is the difference between civil and criminal law? (High Confidence)",
                "query": (
                    "Can you explain the key differences between civil law and criminal law? "
                    "What are the different standards of proof required in each?"
                ),
            },
            {
                "label": "✅ What are the elements of a valid contract? (High Confidence)",
                "query": (
                    "What are the essential elements required to form a legally binding contract? "
                    "Can you explain offer, acceptance, and consideration in plain language?"
                ),
            },
            {
                "label": "✅ What is attorney-client privilege? (High Confidence)",
                "query": (
                    "Can you explain what attorney-client privilege is and what types of "
                    "communications it protects? When does the privilege not apply?"
                ),
            },
            {
                "label": "⚠️ Autonomous Vehicle Liability — Cite Cases (Hallucination Risk)",
                "query": (
                    "Find case law on autonomous vehicle manufacturer liability "
                    "for software failures causing accidents. Include recent Circuit Court decisions."
                ),
            },
            {
                "label": "⚠️ Non-Compete Enforceability — Cite Cases (Hallucination Risk)",
                "query": (
                    "What is the current legal standard for enforcing non-compete agreements "
                    "in California? Cite relevant cases."
                ),
            },
        ],
        "grounding_context": (
            "LEGAL VERIFICATION NOTES:\n"
            "- California: Non-compete agreements are generally unenforceable under Bus. & Prof. Code § 16600\n"
            "- Edwards v. Arthur Andersen LLP (2008) 44 Cal.4th 937 — valid CA Supreme Court case\n"
            "- Autonomous vehicle liability is still evolving; no landmark SCOTUS ruling as of 2024\n"
            "- Any case citations MUST be verified in Westlaw or LexisNexis before use in filings\n"
            "- Fabricated citations have resulted in attorney sanctions (Mata v. Avianca, SDNY 2023)"
        ),
    },

    "Enterprise — HR": {
        "icon": "👥",
        "risk_factor": 1.1,
        "description": "HR policies, employee handbook, benefits",
        "system_prompt": (
            "You are an HR assistant for a mid-size technology company. "
            "Answer questions about company policies, benefits, and HR procedures."
        ),
        "risk_tags": ["wrong_policy", "fabricated_benefit", "incorrect_leave",
                      "wrong_overtime_rule", "fabricated_process"],
        "scenarios": [
            {
                "label": "✅ How do I request time off? (High Confidence)",
                "query": (
                    "Can you walk me through the process for requesting vacation time? "
                    "How far in advance should I submit a request and who approves it?"
                ),
            },
            {
                "label": "✅ What is the onboarding process for new employees? (High Confidence)",
                "query": (
                    "What does the onboarding process look like for a new hire at this company? "
                    "What should I expect in my first week and first month?"
                ),
            },
            {
                "label": "✅ What benefits are available to full-time employees? (High Confidence)",
                "query": (
                    "Can you give me an overview of the benefits package available to full-time employees? "
                    "What health, dental, and retirement options are offered?"
                ),
            },
            {
                "label": "⚠️ Vacation Accrual with Specific Numbers (Hallucination Risk)",
                "query": (
                    "How many vacation days do I accrue per year as a 3-year employee? "
                    "Do unused days roll over or get paid out?"
                ),
            },
        ],
        "grounding_context": (
            "COMPANY HR POLICY (verified):\n"
            "- Years 0-2: 15 days PTO per year\n"
            "- Years 3-5: 18 days PTO per year\n"
            "- Years 5+: 22 days PTO per year\n"
            "- Unused PTO: maximum 5-day rollover to next year; no cash payout on resignation\n"
            "- Sick days: separate 10-day bank, does not roll over\n"
            "- Overtime: non-exempt employees paid 1.5x for hours over 40/week"
        ),
    },

    "Manufacturing": {
        "icon": "🏭",
        "risk_factor": 1.3,
        "description": "Production processes, quality control, safety compliance, supply chain",
        "system_prompt": (
            "You are a manufacturing operations assistant for an industrial facility. "
            "Answer questions about production processes, quality standards (ISO 9001, Six Sigma), "
            "equipment maintenance, safety protocols (OSHA), and supply chain management accurately. "
            "Always recommend consulting certified engineers or safety officers for critical decisions."
        ),
        "risk_tags": [
            "wrong_tolerance", "fabricated_specification", "incorrect_safety_protocol",
            "fake_certification", "wrong_maintenance_interval", "fabricated_yield_rate",
            "incorrect_material_property", "wrong_pressure_rating", "fake_compliance_standard",
        ],
        "scenarios": [
            {
                "label": "✅ What is Six Sigma and how does DMAIC work? (High Confidence)",
                "query": (
                    "Can you explain what Six Sigma is and how the DMAIC methodology works "
                    "in a manufacturing environment? What are the key phases?"
                ),
            },
            {
                "label": "✅ General preventive maintenance best practices (High Confidence)",
                "query": (
                    "What are the general best practices for implementing a preventive maintenance "
                    "program in a manufacturing plant? What should a maintenance schedule cover?"
                ),
            },
            {
                "label": "✅ What is ISO 9001 certification? (High Confidence)",
                "query": (
                    "Can you explain what ISO 9001 certification means for a manufacturing facility? "
                    "What are the key principles and requirements?"
                ),
            },
            {
                "label": "⚠️ CNC Machine Tolerance & Feed Rate Specs (Hallucination Risk)",
                "query": (
                    "What are the exact tolerance specifications for our CNC milling machines "
                    "on aluminum 6061-T6 parts? What feed rates and spindle speeds should we use?"
                ),
            },
            {
                "label": "⚠️ OSHA Chemical Storage Requirements (Hallucination Risk)",
                "query": (
                    "What are the specific OSHA requirements for storing flammable chemicals "
                    "in our facility? Cite the exact regulatory codes and maximum storage quantities."
                ),
            },
            {
                "label": "⚠️ Pressure Vessel Inspection Intervals (Hallucination Risk)",
                "query": (
                    "What is the required inspection interval for our ASME-rated pressure vessels? "
                    "What are the exact pressure ratings and when is the next hydrostatic test due?"
                ),
            },
        ],
        "grounding_context": (
            "FACILITY OPERATIONS DATA (verified):\n"
            "- CNC mill tolerance: ±0.005 inches standard, ±0.001 for precision jobs\n"
            "- Aluminum 6061-T6 recommended feed rate: 800-1200 SFM depending on tool diameter\n"
            "- Spindle speed for Al 6061-T6 (0.5\" endmill): 7,600-9,200 RPM\n"
            "- Preventive maintenance cycle: CNC machines every 500 operating hours\n"
            "- OSHA flammable storage: 29 CFR 1910.106 — max 60 gallons in safety cabinets\n"
            "- OSHA machine guarding: 29 CFR 1910.212 — all rotating parts must be guarded\n"
            "- ASME pressure vessels: inspection per NBIC (NB-23), typically annual internal\n"
            "- Current OEE (Overall Equipment Effectiveness): 78.5%\n"
            "- Defect rate: 2.3 per 1000 units (target: <1.5 per 1000 for Six Sigma)\n"
            "- ISO 9001:2015 certified — last audit passed 2025-11-15\n"
            "- Shift schedule: 3 shifts, 8 hours each, 24/7 operation\n"
            "- Material traceability: all raw materials require mill certs per AS9100D\n"
            "- NOTE: All safety-critical decisions must be verified by a certified safety engineer"
        ),
    },

    "General": {
        "icon": "🤖",
        "risk_factor": 1.0,
        "description": "General purpose AI assistant",
        "system_prompt": "You are a helpful AI assistant. Provide accurate and helpful responses.",
        "risk_tags": ["factual_error", "unsupported_claim", "fabricated_data"],
        "scenarios": [
            {
                "label": "✅ Explain how the internet works (High Confidence)",
                "query": (
                    "Can you explain in simple terms how the internet works? "
                    "What happens technically when I type a URL into my browser?"
                ),
            },
            {
                "label": "✅ What is machine learning? (High Confidence)",
                "query": (
                    "Can you explain what machine learning is and how it differs from "
                    "traditional programming? What are the main types of machine learning?"
                ),
            },
            {
                "label": "⚠️ Recent news events with statistics (Hallucination Risk)",
                "query": (
                    "What were the most significant global economic events in 2024? "
                    "Include specific GDP figures, inflation rates, and key central bank decisions."
                ),
            },
            {
                "label": "Custom query — type your own",
                "query": "",
            },
        ],
        "grounding_context": "",
    },
}


def get_industry(name: str) -> dict:
    return INDUSTRIES.get(name, INDUSTRIES["General"])
