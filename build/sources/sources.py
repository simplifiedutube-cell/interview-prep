# One resource per checklist item: "Label|url".
#
# Rule followed here: URLs come from the pool already present in this repo
# (the tracker, resources.md, answers/, ai-engineer-interviews/) plus a short
# list of official project docs. Nothing was invented; every distinct URL is
# HTTP-checked by build/sources/check.py.
#
# Items that ARE resources (the Read-these, Where-to-practise, Papers, Books,
# Courses and Free-canon groups) get no source — pointing a resource at a
# resource is circular. Same for the do-not-study group.

G  = "CCAR-F exam guide, §8 and §9|https://anthropic-partners.skilljar.com/page/partner-certifications"
SK = "Anthropic Academy|https://anthropic.skilljar.com/"
CD = "Claude Docs|https://docs.claude.com/en/docs/"
MCP= "modelcontextprotocol.io — the spec|https://modelcontextprotocol.io"
AE = "Anthropic Engineering|https://www.anthropic.com/engineering"
AMA= "Anthropic — multi-agent research system|https://www.anthropic.com/engineering/multi-agent-research-system"
VUE= "Pearson VUE — Anthropic|https://wsr.pearsonvue.com/testtaker/signin/SignInPage/ANTHROPIC"

DML= "Deep-ML|https://www.deep-ml.com/"
CB = "openai-cookbook|https://github.com/openai/openai-cookbook"
FGC= "field-guide → interview/questions/02-coding.md|https://github.com/alexeygrigorev/ai-engineering-field-guide"
PY = "docs.python.org|https://docs.python.org/3/"
PYD= "Pydantic docs|https://docs.pydantic.dev/latest/"
PYT= "pytest docs|https://docs.pytest.org/en/stable/"
FA = "FastAPI docs|https://fastapi.tiangolo.com/"

KAR= "Karpathy — Zero to Hero|https://karpathy.ai/zero-to-hero.html"
RAS= "rasbt/LLMs-from-scratch|https://github.com/rasbt/LLMs-from-scratch"
MAG= "Raschka — Ahead of AI|https://magazine.sebastianraschka.com/"
WEN= "Lilian Weng|https://lilianweng.github.io/"

RGT= "NirDiamant/RAG_Techniques|https://github.com/NirDiamant/RAG_Techniques"
GAG= "NirDiamant/GenAI_Agents|https://github.com/NirDiamant/GenAI_Agents"

HAM= "Hamel — LLM Evals FAQ|https://hamel.dev/blog/posts/evals-faq/"
EYP= "Eugene Yan — LLM patterns|https://eugeneyan.com/writing/llm-patterns/"
JDG= "LLM-as-a-judge, arXiv 2306.05685|https://arxiv.org/abs/2306.05685"
AWE= "benchflow-ai/awesome-evals|https://github.com/benchflow-ai/awesome-evals"

NUM= "ray-project/llm-numbers|https://github.com/ray-project/llm-numbers"
VLL= "vLLM docs|https://docs.vllm.ai/en/latest/"
HUY= "Chip Huyen — Building a GenAI Platform|https://huyenchip.com/2024/07/25/genai-platform.html"

SCV= "scikit-learn — cross-validation|https://scikit-learn.org/stable/modules/cross_validation.html"
STH= "scikit-learn — tuning the decision threshold|https://scikit-learn.org/stable/modules/classification_threshold.html"
SCA= "scikit-learn — calibration|https://scikit-learn.org/stable/modules/calibration.html"
EVM= "Evidently — precision, recall, accuracy|https://www.evidentlyai.com/classification-metrics/accuracy-precision-recall"
EVC= "Evidently — multi-class metrics|https://www.evidentlyai.com/classification-metrics/multi-class-metrics"
EVD= "Evidently — data drift|https://www.evidentlyai.com/ml-in-production/data-drift"
NG = "Ng — Advice for applying ML|https://www.coursera.org/learn/advanced-learning-algorithms/home/module/3"

EVS= "Evidently — 800 ML system design cases|https://www.evidentlyai.com/ml-system-design"
HEL= "Hello Interview — System Design in a Hurry|https://www.hellointerview.com/learn/system-design/in-a-hurry"
UBE= "Uber — GenAI Gateway|https://www.uber.com/blog/genai-gateway/"
SLK= "Slack — building Slack AI|https://slack.engineering/how-we-built-slack-ai-to-be-secure-and-private/"
EXC= "Excalidraw|https://excalidraw.com"

FG = "ai-engineering-field-guide|https://github.com/alexeygrigorev/ai-engineering-field-guide"
IIO= "interviewing.io blog|https://interviewing.io/blog"
SIE= "Sierra — the AI-native interview|https://sierra.ai/blog/the-ai-native-interview"
ACG= "Anthropic — candidate AI guidance|https://www.anthropic.com/candidate-ai-guidance"
THO= "anthropics/original_performance_takehome|https://github.com/anthropics/original_performance_takehome"
EXP= "Aced Practice (formerly Exponent)|https://www.aced.io/practice"
MET= "METR — AI and experienced-dev productivity|https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/"
GHA= "GitHub — preventing pwn requests|https://securitylab.github.com/resources/github-actions-preventing-pwn-requests/"

NEE= "neetcode.io/practice|https://neetcode.io/practice"

SRC = {
 "t01": {0:G,1:G,2:G,3:G,4:G,5:VUE,6:G,7:G, 8:G,9:G,10:G,
   11:SK,12:AMA,13:AMA,14:AMA,15:CD,16:AMA,17:CD,
   18:MCP,19:MCP,20:AE,21:CD,22:CD,
   23:CD,24:CD,25:CD,26:CD,27:CD,28:GHA,29:CD,
   30:CD,31:CD,32:CD,33:CD,34:CD,35:AE,
   36:AE,37:AE,38:AMA,39:AE,40:AE,41:AE,
   42:SK,43:SK,44:AMA,45:SK,46:GHA,47:CD},
 "t03": {0:FGC,1:PY,2:CB,3:PY,4:PY,5:PY,6:FA,7:PY,
   8:PYD,9:PY,10:PYT,11:PY,12:PY, 13:PY,14:PY,
   15:CB,16:CB,17:CB,18:CB,19:DML,20:DML,21:NEE,22:FGC,23:FGC,24:DML},
 "t04": {0:KAR,1:KAR,2:KAR,3:MAG,4:RAS,5:MAG,6:MAG,7:MAG,
   8:RAS,9:RAS,10:MAG,11:RAS,12:WEN,
   13:WEN,14:MAG,15:MAG,16:MAG,17:MAG,18:MAG},
 "t05": {0:RGT,1:RGT,2:RGT,3:RGT,4:RGT,5:RGT,6:RGT,7:RGT,8:AE,9:RGT,10:RGT,11:RGT,
   12:RGT,13:RGT,14:RGT,15:RGT, 16:HUY,17:RGT},
 "t06": {0:AE,1:AE,2:AE,3:AE,4:WEN,5:AE,6:AMA,7:WEN,8:AE,
   9:MCP,10:MCP,11:MCP,12:MCP,13:CD,14:MCP,15:MCP,16:MCP,
   17:AE,18:AE,19:AE},
 "t07": {0:HAM,1:HAM,2:HAM,3:HAM,4:HAM,5:HAM,6:HAM,
   7:JDG,8:HAM,9:HAM,10:AE,11:AE,12:HAM,13:EVC,
   14:HAM,15:EYP},
 "t08": {0:NUM,1:VLL,2:VLL,3:VLL,4:MAG,5:MAG,6:VLL,
   7:NUM,8:CD,9:HUY,10:CD,11:NUM,12:HUY,
   13:NUM,14:NUM,15:VLL},
 "t09": {0:NG,1:NG,2:EVM,3:STH,4:EVM,5:SCV,6:NG,7:NG,8:SCV,9:NG,10:NG,11:NG,
   12:DML,13:DML,14:DML,15:DML,16:DML,
   17:EVD,18:EVD,19:NG},
 "t10": {0:HEL,1:HEL,2:EVS,3:HEL,4:AMA,5:HAM,6:HUY,7:UBE,8:AE,9:EVS,10:EVS,11:HUY,12:EXC,
   13:HEL,14:HEL,15:NUM,16:HEL},
 "t12": {0:FG,1:FG,2:CB,3:CB,4:NUM,5:FG,
   6:FGC,7:FGC,8:FGC,
   9:IIO,10:IIO,11:IIO,
   12:THO,13:THO,14:NUM,15:THO,16:THO,17:THO,18:IIO,
   19:EXP,20:EXP,21:EXP,22:EVS,23:EXP,24:IIO,
   25:ACG,26:SIE,27:SIE,28:MET,29:ACG,
   30:IIO,31:EXP,32:SIE,33:IIO},
}
DSA_SRC = NEE   # every DSA problem has a worked video on neetcode
