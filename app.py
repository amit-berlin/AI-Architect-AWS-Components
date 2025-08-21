"""
AI Architect with AWS Components (Slider-Driven Version)
- User sets 10 critical parameters with sliders.
- 10 AI Architect Agents reason based on sliders.
- Final AWS-based AI Architecture dynamically proposed + diagram.
"""

import streamlit as st

st.set_page_config(page_title="AI Architect with AWS Components", layout="wide")

st.title("🤖 AI Architect with AWS Components")
st.caption("Set 10 architectural parameters below. Agentic AI Architects will propose an AWS-based architecture dynamically.")

# --------------------------
# 10 Parameters via Sliders
# --------------------------
st.sidebar.header("⚙️ Configure AI Architecture Parameters")

params = {
    "Data Volume (1=GB, 10=PB)": st.sidebar.slider("Data Volume", 1, 10, 5),
    "Data Variety (1=structured, 10=multi-modal)": st.sidebar.slider("Data Variety", 1, 10, 5),
    "Real-Time Requirement (1=batch, 10=real-time)": st.sidebar.slider("Real-Time Requirement", 1, 10, 5),
    "Model Complexity (1=basic ML, 10=advanced GenAI)": st.sidebar.slider("Model Complexity", 1, 10, 7),
    "Scalability Need (1=small, 10=global enterprise)": st.sidebar.slider("Scalability Need", 1, 10, 8),
    "Security & Compliance (1=basic, 10=finance/healthcare)": st.sidebar.slider("Security & Compliance", 1, 10, 9),
    "Integration Needs (1=standalone, 10=deep ERP/SAP)": st.sidebar.slider("Integration Needs", 1, 10, 6),
    "Cost Sensitivity (1=performance, 10=cost savings)": st.sidebar.slider("Cost Sensitivity", 1, 10, 5),
    "Automation (1=manual, 10=full CI/CD)": st.sidebar.slider("Automation & CI/CD", 1, 10, 7),
    "User Experience (1=API only, 10=rich end-user app)": st.sidebar.slider("User Experience Priority", 1, 10, 6),
}

# --------------------------
# Agent Roles
# --------------------------
AGENT_ROLES = [
    "Data Ingestion & Storage",
    "Processing & ETL",
    "Modeling & LLMs",
    "Knowledge Graph & Search",
    "Integration",
    "Infrastructure & Deployment",
    "Scalability",
    "Monitoring & Observability",
    "Security & Compliance",
    "UX & APIs"
]

# --------------------------
# Agent Proposals (based on slider values)
# --------------------------
st.markdown("## 🔎 10 Agent Proposals")

def map_services(params):
    """Map slider values to AWS service recommendations."""
    services = set(["S3"])  # Always central
    
    if params["Data Volume (1=GB, 10=PB)"] > 7:
        services.update(["Redshift", "Glue"])
    else:
        services.update(["RDS", "DynamoDB"])
    
    if params["Data Variety (1=structured, 10=multi-modal)"] > 6:
        services.update(["S3", "OpenSearch", "Kendra"])
    
    if params["Real-Time Requirement (1=batch, 10=real-time)"] > 6:
        services.update(["Kinesis", "MSK", "Lambda"])
    
    if params["Model Complexity (1=basic ML, 10=advanced GenAI)"] > 6:
        services.update(["Bedrock", "SageMaker"])
    else:
        services.update(["Comprehend"])
    
    if params["Scalability Need (1=small, 10=global enterprise)"] > 7:
        services.update(["ECS Fargate", "EKS", "CloudFront"])
    else:
        services.update(["Lambda", "API Gateway"])
    
    if params["Security & Compliance (1=basic, 10=finance/healthcare)"] > 7:
        services.update(["IAM", "KMS", "GuardDuty", "Macie"])
    else:
        services.update(["IAM"])
    
    if params["Integration Needs (1=standalone, 10=deep ERP/SAP)"] > 7:
        services.update(["AppFlow", "StepFunctions"])
    
    if params["Cost Sensitivity (1=performance, 10=cost savings)"] > 7:
        services.update(["S3 Intelligent-Tiering", "Spot Instances"])
    
    if params["Automation (1=manual, 10=full CI/CD)"] > 6:
        services.update(["CodePipeline", "CodeBuild"])
    
    if params["User Experience (1=API only, 10=rich end-user app)"] > 6:
        services.update(["Amplify", "CloudFront", "QuickSight"])
    
    return services

# Run agents
all_services = map_services(params)
cols = st.columns(2)
for i, role in enumerate(AGENT_ROLES):
    with cols[i % 2]:
        st.markdown(f"### {i+1}. {role}")
        st.write(f"As {role}, I recommend AWS components based on your parameters.")
        st.write(f"**Candidate Services:** {', '.join(sorted(all_services))}")

# --------------------------
# Synthesized Architecture
# --------------------------
st.markdown("---")
st.markdown("## 🏗️ Synthesized AWS Architecture")

st.success("✅ Final selected AWS services:")
st.write(", ".join(sorted(all_services)))

# --------------------------
# Architecture Diagram
# --------------------------
st.markdown("## 🗺️ AWS Architecture Diagram")

dot_lines = [
    "digraph AWSArch {",
    "rankdir=LR;",
    'node [shape=box, style="rounded,filled", fillcolor="#F2F4F8"];'
]

# Add nodes
for s in all_services:
    dot_lines.append(f'"{s}" [label="{s}"];')

# Core flow
edges = [
    ("Client", "API Gateway"),
    ("API Gateway", "Lambda"),
    ("Lambda", "S3"),
    ("Lambda", "Redshift"),
    ("Lambda", "OpenSearch"),
    ("Lambda", "Bedrock"),
    ("Lambda", "SageMaker"),
    ("Lambda", "Comprehend"),
    ("Lambda", "Neptune"),
    ("Lambda", "Kinesis"),
    ("Lambda", "CodePipeline"),
    ("Lambda", "CloudWatch"),
]
for a, b in edges:
    if a in all_services or a == "Client":
        if b in all_services:
            dot_lines.append(f'"{a}" -> "{b}";')

dot_lines.append("}")
st.graphviz_chart("\n".join(dot_lines), use_container_width=True)

# --------------------------
# Final Notes
# --------------------------
st.markdown("## 📌 Final Notes")
st.write("This AI Architect app dynamically reasons using 10 architectural parameters. "
         "It selects AWS components, synthesizes an enterprise-grade design, and generates a diagram. "
         "Sliders let you think like an AI Architect — adjusting trade-offs to reshape the architecture.")
