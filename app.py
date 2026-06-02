from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# ---------------- Logs ----------------
LOGS = {
    "kingl3ss world": [
        "[2025/09/27/00:41] Dr-R3D > Secure channel established.",
        "[2025/09/27/00:41] 3ch03119 > Speak.",
        "[2025/09/27/00:42] Dr-R3D > I’m transmitting everything I have.",
        "[2025/09/27/00:42] Dr-R3D > This stays off Foundation records.",
        "[2025/09/27/00:43] 3ch03119 > Begin with designation.",
        "[2025/09/27/00:44] Dr-R3D > PF-001.",
        "[2025/09/27/00:44] Dr-R3D > That’s the only identifier they allow.",
        "[2025/09/27/00:45] 3ch03119 > Not sufficient.",
        "[2025/10/01/18:12] Dr-R3D > There is no discovery file.",
        "[2025/10/01/18:12] Dr-R3D > No origin point. No retrieval event.",
        "[2025/10/01/18:13] Dr-R3D > PF-001 exists in the system as if it was always accounted for.",
        "[2025/10/01/18:14] 3ch03119 > Behavior.",
        "[2025/10/04/03:27] Dr-R3D > It does not react to stimulus.",
        "[2025/10/04/03:28] Dr-R3D > It alters surrounding data instead.",
        "[2025/10/04/03:28] Dr-R3D > Logs desynchronize.",
        "[2025/10/04/03:28] Dr-R3D > Some records go public.",
        "[2025/10/04/03:29] 3ch03119 > Intent.",
        "[2025/10/04/03:30] Dr-R3D > Unknown.",
        "[2025/10/04/03:30] Dr-R3D > But the alterations are not random.",
        "[2025/10/09/22:06] Dr-R3D > I found patterns in the corruption.",
        "[2025/10/09/22:06] Dr-R3D > Gaps between certain logs prevent breaches.",
        "[2025/10/09/22:07] Dr-R3D > They form sequences.",
        "[2025/10/09/22:08] 3ch03119 > Sequences of what.",
        "[2025/10/09/22:09] Dr-R3D > Outcomes.",
        "[2025/10/09/22:09] Dr-R3D > Or something comparable.",
        "[2025/10/15/01:51] 3ch03119 > Foundation response.",
        "[2025/10/15/01:52] Dr-R3D > They are not containing it.",
        "[2025/10/15/01:52] Dr-R3D > They are preparing a procedure.",
        "[2025/10/15/01:53] Dr-R3D > They call it “alignment.”",
        "[2025/10/15/01:54] 3ch03119 > Alignment with what.",
        "[2025/10/15/01:55] Dr-R3D > They will not say.",
        "[2025/10/15/01:55] Dr-R3D > Every internal model references a “rebirth state.”",
        "[2025/10/22/20:33] Dr-R3D > Messages changed after the meeting.",
        "[2025/10/22/20:34] Dr-R3D > Failure prediction was discontinued.",
        "[2025/10/22/20:34] Dr-R3D > They now correct failures instead.",
        "[2025/10/22/20:35] 3ch03119 > Including yours.",
        "[2025/10/22/20:36] Dr-R3D > Yes. Including mine.",
        "[2025/10/30/04:18] Dr-R3D > That’s why I’m sending this to you.",
        "[2025/10/30/04:18] Dr-R3D > You are the only contact not affected.",
        "[2025/10/30/04:19] Dr-R3D > If PF-001 is even an entity.",
        "[2025/10/30/04:19] Dr-R3D > You asked what PF-001 removes.",
        "[2025/10/30/04:19] Dr-R3D > It does not remove.",
        "[2025/10/30/04:20] Dr-R3D > It changes.",
        "[2025/10/30/04:20] 3ch03119 > Final conclusion.",
        "[2025/10/30/04:21] Dr-R3D > PF-001 is not an anomaly.",
        "[2025/10/30/04:21] Dr-R3D > It is a breach point.",
        "[2025/10/30/04:22] Dr-R3D > The Foundation is attempting to realign the world around it.",
        "[2025/10/30/04:23] 3ch03119 > Continue observation.",
        "[2025/10/30/04:23] 3ch03119 > Do not interfere.",
        "[2025/10/30/04:23] 3ch03119 > At all costs, do not let them enter CARC0SA."
    ],
    "carc0sa": [
        "[????/??/??/??:??] FOUNDATION ARCHIVE ACCESS",
        "[STATUS: DEGRADED]",
        "",
        "[LOG_ID: CARCOSA-OBS-07]",
        "",
        "[2025/08/19/02:11]Observer> Initial reference to \"Carcosa\" located.",
        "[2025/08/19/02:11]Observer> No physical coordinates attached.",
        "01010100 01101000 01100101 00100000 01001011",
        "[2025/08/19/02:12]Observer> Treated as conceptual location. Possibly memetic.",
        "",
        "[2025/08/21/17:44]Observer> Cross-referencing mentions.",
        "[2025/08/21/17:45]Observer> Carcosa appears only in corrupted files,",
        "01101001 01100110 01110100 01110011 00100000",
        "redacted testimonies,",
        "01110100 01101000 01110010 01101111 01110101 01100111 01101000",
        "and dreams recorded during REM monitoring.",
        "",
        "[2025/08/25/03:02]Observer> Repeated descriptors detected:",
        "- twin suns",
        "- black stars",
        "01001011 01010010 01000101 01000100 01000001 01000011 01010100 01000101 01000100",
        "- a city that should not persist",
        "- the lake (name missing)",
        "",
        "[2025/09/02/00:19]Observer> Psychological effects noted.",
        "[2025/09/02/00:20]Observer> Subjects exposed to the name alone exhibit:",
        "- déjà vu",
        "- grief without source",
        "01100001 00100000 01110111 01101000 01101001 01110011 01110000 01100101 01110010",
        "- certainty they have \"left something behind\"",
        "",
        "[2025/09/10/21:57]Observer> Attempted mapping failed.",
        "[2025/09/10/21:58]Observer> All diagrams converge into impossible geometry.",
        "01110011 01110100 01110010 01100101 01100101 01110100 01110011 00101100",
        "[2025/09/10/21:58]Observer> Angles do not agree with each other.",
        "",
        "[2025/09/14/04:33]Observer> New correlation.",
        "[2025/09/14/04:34]Observer> References to Carcosa spike during discussions of:",
        "- kingship",
        "- absence",
        "01110100 01110111 01101001 01110011 01110100",
        "- return events",
        "- alignment procedures",
        "",
        "[2025/09/20/01:06]Observer> WARNING:",
        "[2025/09/20/01:06]Observer> System auto-completed \"Carcosa\" with:",
        "01101000 01101001 01110011 00100000 01100111 01100001 01111010 01100101",
        "[2025/09/20/01:07]Observer> Entry removed.",
        "",
        "[2025/09/22/23:41]Observer> Memory discrepancy detected.",
        "[2025/09/22/23:41]Observer> I am certain I have never been there.",
        "01110111 01101000 01101111 00100000 01100110 01101111 01101100 01101100 01101111 01110111",
        "[2025/09/22/23:42]Observer> I am equally certain I left.",
        "",
        "[2025/09/22/23:43]Observer> Terminating log before further contamination.",
        "01110100 01101000 01100101 00100000 01100110 01100001 01101001 01101110 01110100",
        "",
        "[END_LOG]",
        "",
        "01101001 01110100 01110011 00100000 01110100 01101111 00100000 01110010 01100101 01101101 01100101 01101101 01100010 01100101 01110010 00100000 01101000 01101001 01101101 00101110"
    ],
    "pf-001": [
        "20", "8", "5", "4", "15", "3", "20", "15", "18", "12", "9", "5",
        "19", "1", "18", "5", "13", "15", "18", "5", "20", "18", "21",
        "20", "8", "6", "21", "12", "20", "8", "5", "12", "15", "14",
        "7", "5", "18", "20", "8", "5", "13", "1", "4", "14", "5",
        "19", "19", "21", "14", "6", "15", "12", "4", "19"
    ],
    "rebirth state": [
        "[LOG-ALPHA]",
        "",
        "Presence without warning.",
        "Witnesses remain unreliable.",
        "Judgement deferred indefinitely.",
        "",
        "[END]"
    ],
    "black stars": [
        "[LOG-BETA]",
        "",
        "Assume the following:",
        "",
        "a = anomaly",
        "b = baseline",
        "c = correction",
        "O = outcome",
        "",
        "Stability Index S is defined as:",
        "",
        "S = (a + c) − (a − 2b) + O",
        "",
        "Note:",
        "- anomaly values cancel during alignment",
        "- corrections are discarded post-calculation",
        "",
        "Only persistent terms are recorded.",
        "",
        "[END]"
    ],
    "deja vu": [
        "[LOG-GAMMA]",
        "",
        "l u k",
        "",
        "[END]"
    ],
    "alignment": [
        "[LOG-DELTA]",
        "",
        "Last confirmed activity:",
        "4:23 pM",
        "",
        "No further network breach detected.",
        "",
        "[END]"
    ],
    "absence": [
        "[LOG-ECHO]",
        "",
        "↑ = elevate",
        "↓ = suppress",
        "N = unknown variable",
        "",
        "↑",
        "↑",
        "↑",
        "N",
        "↓",
        "↑",
        "↓",
        "↑",
        "↑",
        "↓",
        "↑",
        "",
        "[END]"
    ]
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_log", methods=["POST"])
def get_log():
    data = request.get_json(silent=True) or {}
    code = data.get("code", "").lower()
    if code in LOGS:
        return jsonify({"success": True, "log": LOGS[code]})
    else:
        return jsonify({"success": False, "log": ["Unknown code."]})

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)