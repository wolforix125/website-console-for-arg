from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# ---------------- Logs ----------------
LOGS = {
    "": [
	"[1986/05/19-00:00] > Initialising...",
	"[1986/05/19-00:00] > ...",
	"[1986/05/19-00:00] > ...",
	"[1986/05/19-00:00] > System Confirmed Online.",
	"[1986/05/19-00:00] > Welcome to the Log Database and Recording Archive.",
	"[1986/05/19-00:00] > Operations restricted by the Silent Preacher Corporation.",
	"[1986/05/19-00:00] > Internal access only.",
	"[1986/05/19-00:00] > If you are reading this you have been granted access.",
	"[1986/05/19-00:00] > If you have not been granted access.",
	"[1986/05/19-00:00] > Your location will be recorded and inspected for unusual activity.",
	"[1986/05/19-00:00] > initiating identification scanner.",
	"[1986/05/19-00:00] > UNAUTHORISED ENTRY DETEC--.",
	"[1986/05/19-00:00] > Master Bypass Detected.",
	"[1986/05/19-00:00] > location and log in logs will be deleted upon exit.",
	"[2005/03/15-21:46] > WELCOME TO THE BACKEND DO YOUR BUSINESS AND LEAVE... AND DONT FORGET OUR DEAL!!!",
	"[1986/05/19-00:00] > Proceed to [log0]."
    ],
    "log0": [
	"[1986/05/19-00:01] > Loading LOG0."
	"[1986/05/19-00:01] > ..."
	"[1986/05/19-00:01] > LOG0 designation: SYSTEM ORIENTATION."
	"[1986/05/19-00:01] > This log is pre-loaded for all new users."
	"[1986/05/19-00:01] > Read carefully."
	"[1986/05/19-00:01] > You will not be reminded of this information again."
	"[1986/05/19-00:01] > Although you will be able to access this log any time you please."
	""
	""
	"[1986/05/19-00:02] > WHAT THIS SYSTEM IS."
	"[1986/05/19-00:02] > ..."
	"[1986/05/19-00:02] > The Log Database and Recording Archive contains every file,"
	"[1986/05/19-00:02] > Every transmission, every recording, and every internal document"
	"[1986/05/19-00:02] > Produced by or relating to the Silent Preacher Corporation"
	"[1986/05/19-00:02] > And its ongoing containment operations."
	"[1986/05/19-00:03] > This includes personnel records."
	"[1986/05/19-00:03] > Incident reports."
	"[1986/05/19-00:03] > Materials that have not been formally classified."
	"[1986/05/19-00:03] > Materials that have been formally classified"
	"[1986/05/19-00:03] > And subsequently overruled for access by directorial order."
	"[1986/05/19-00:04] > And things that should not exist in a database."
	"[1986/05/19-00:04] > They are here anyway."
	"[1986/05/19-00:04] > We stopped asking why."
	""
	""
	"[1986/05/19-00:05] > HOW TO NAVIGATE THIS SYSTEM."
	"[1986/05/19-00:05] > ..."
	"[1986/05/19-00:05] > All files in this archive are assigned a log number."
	"[1986/05/19-00:05] > To access a file type:"
	"[1986/05/19-00:05] > log lowercase followed by the number of the file you wish to access."
	"[1986/05/19-00:06] > Example:"
	"[1986/05/19-00:06] > log0 — this file. System orientation. You are reading it now."
	"[1986/05/19-00:06] > log1 — first entry in the archive."
	"[1986/05/19-00:06] > log2 — second entry. And so on."
	"[1986/05/19-00:07] > ..."
	"[1986/05/19-00:07] > some logs will be capetelized e.g [EXAMPLE] please lowercase these to access the neccesary file"
	"[1986/05/19-00:07] > Files may be text logs, audio transcripts, internal memos,"
	"[1986/05/19-00:07] > personnel documents, or direct recordings."
	"[1986/05/19-00:07] > The system will tell you what you are opening before you open it."
	"[1986/05/19-00:08] > You will not have the option to stop the log from getting played."
	"[1986/05/19-00:08] > you may refresh the page to clear your page."
	""
	""
	"[1986/05/19-00:09] > WHAT THIS ARCHIVE CONTAINS."
	"[1986/05/19-00:09] > ..."
	"[1986/05/19-00:09] > This archive was assembled following the events of"
	"[1986/05/19-00:09] > May 10th and the unresolved status of the foundations founder"
	"[1986/05/19-00:09] > [EDIT]"
	"[1986/05/19-00:09] > this archive has not been used until septembet 14th year 2005 due to employee"
	"[1986/05/19-00:09] > Spencer Cole case ref: SC-014."
	"[1986/05/19-00:10] > It contains all materials relevent to that case."
	"[1986/05/19-00:10] > as well as all prior materials that provide necessary context."
	"[1986/05/19-00:10] > You are advised to access logs in order."
	"[1986/05/19-00:10] > You are not required to."
	"[1986/05/19-00:11] > ..."
	""
	""
	"[1986/05/19-00:12] > CONTENT ADVISORY."
	"[1986/05/19-00:12] > ..."
	"[1986/05/19-00:12] > Some files in this archive contain audio recorded"
	"[1986/05/19-00:12] > in proximity to the object designated internally as"
	"[1986/05/19-00:12] > THE UNDERNINE OBJECT."
	"[1986/05/19-00:13] > These files have been reviewed by our technical team."
	"[1986/05/19-00:13] > Several sections could not be fully resolved."
	"[1986/05/19-00:13] > Several sections contain audio our team cannot account for."
	"[1986/05/19-00:13] > These sections have not been removed."
	"[1986/05/19-00:14] > Removing them was considered however."
	"[1986/05/19-00:14] > The decision was made to leave the archive intact."
	"[1986/05/19-00:14] > You will know these sections when you reach them."
	"[2025/10/14-00:16] > There is a file in this system with seven names on it."
	"[2025/10/14-00:16] > Case ref: [MARK-CARRIERS] / FULL LIST."
	"[2025/10/14-00:17] > this contains all currently known individuals who have entered,"
	"[2025/10/14-00:17] > the tunnel leading to the [UNDERNINE OBJECT]"
	""
	""
	"[2025/10/14-00:18] > ONE FINAL NOTE."
	"[2025/10/14-00:18] > ..."
	"[2025/10/14-00:18] > This system was designed to store and provide access to information."
	"[2025/10/14-00:18] > That is its only function."
	"[2025/10/14-00:19] > However."
	"[2025/10/14-00:19] > Since the events of October 2025.	"
	"[2025/10/14-00:19] > The system has on several occasions added entries	"
	"[2025/10/14-00:19] > that were not submitted by any logged user."
	"[2025/10/14-00:20] > These entries have not been removed."
	"[2025/10/14-00:20] > We do not know who submitted them."
	"[2025/10/14-00:20] > We do not know how."
	"[2025/10/14-00:21] > If you encounter a log that does not appear"
	"[2025/10/14-00:21] > in the official index at the top of this file."
	"[2025/10/14-00:21] > You may access it."
	"[2025/10/14-00:22] > We cannot tell you what it contains."
	"[2025/10/14-00:22] > We cannot tell you where it came from."
	"[2025/10/14-00:22] > We can tell you that the entries are not hostile."
	"[2025/10/14-00:22] > We think."
	"[2025/10/14-00:23] > We have developed a complicated relationship"
	"[2025/10/14-00:23] > with the word think."
	""
	""
	"[2025/10/14-00:24] > END OF LOG0."
	"[2025/10/14-00:24] > ..."
	"[2025/10/14-00:24] > For current available logs access: [INDEX]"
	"[2025/10/14-00:24] > New entries may appear without notice."
	"[2025/10/14-00:25] > Type [INDEX] to begin begin."
	"[2025/10/14-00:25] > ..."
	"[2025/10/14-00:25] > The archive is waiting."
	"[2025/10/14-00:25] > It is good at waiting."
	"[2025/10/14-00:25] > It has had practice."
	"[2025/10/14-00:25] > _____"
	"END LOG"
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