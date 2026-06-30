# -*- coding: utf-8 -*-
"""build.py - 2026 월드컵 페이지 자동 갱신기 (football-data 뼈대 + API-FOOTBALL 라이브)."""
import os, sys, re, json, html, datetime, urllib.request

def flag(code,ko,cls="sflag"):
    return f'<img class="{cls}" src="https://flagcdn.com/{code}.svg" alt="{html.escape(ko)}" loading="lazy">'

# ---------------- DATA: ranking ----------------
R=[
(1,"아르헨티나","Argentina","ar","r32","J조 1위","디펜딩 챔피언. J조 3전 전승, 메시가 또 해냈다. 32강 상대는 최약체 카보베르데."),
(2,"스페인","Spain","es","r32","H조 1위","야말의 스페인. H조 1위지만 카보베르데와 비기는 진땀. 32강서 오스트리아."),
(3,"프랑스","France","fr","r32","I조 1위","I조 3전 전승 +8 압도. 뎀벨레 노르웨이전 해트트릭. 강력한 우승 후보."),
(4,"잉글랜드","England","gb-eng","r32","L조 1위","L조 1위로 무난 통과. 32강 상대는 콩고DR."),
(5,"포르투갈","Portugal","pt","r32","K조 2위","호날두 여전히 선발. K조 2위. 32강 크로아티아와 빅매치."),
(6,"브라질","Brazil","br","r16","C조 1위","16강 1번으로 진출 확정. 일본 2:1 격파. 네이마르 복귀전."),
(7,"모로코","Morocco","ma","r32","C조 2위","2022 4강 신화 재현 노린다. 32강 네덜란드와 대형 매치."),
(8,"네덜란드","Netherlands","nl","r32","F조 1위","F조 1위. 32강서 모로코, 사실상 16강급 대진."),
(9,"벨기에","Belgium","be","r32","G조 1위","더 브라위너와 루카쿠. G조 1위. 32강 세네갈."),
(10,"독일","Germany","de","r32","E조 1위","E조 1위지만 에콰도르에 충격패. 32강 파라과이."),
(11,"크로아티아","Croatia","hr","r32","L조 2위","2018 준우승·2022 3위 노장군단. 32강 포르투갈."),
(12,"이탈리아","Italy","it","noqual","미진출","랭킹 12위인데 본선에 없다. 이번 대회 최대 미스터리."),
(13,"콜롬비아","Colombia","co","r32","K조 1위","K조 1위로 포르투갈·콩고 제침. 32강 가나."),
(14,"멕시코","Mexico","mx","r32","A조 1위","공동 개최국. A조 3전 전승 무실점. 32강 에콰도르."),
(15,"세네갈","Senegal","sn","r32","I조 3위","랭킹 15위인데 I조 3위로 겨우 생존. 32강서 벨기에라는 가시밭길."),
(16,"우루과이","Uruguay","uy","groupout","H조 3위","랭킹 16위의 굴욕. H조 3위로 조별 탈락. 본선 최고 랭킹 탈락팀."),
(17,"미국","USA","us","r32","D조 1위","공동 개최국. D조 1위지만 마지막날 튀르키예에 덜미. 32강 보스니아."),
(18,"일본","Japan","jp","r32out","F조 2위","강호 중 첫 탈락. 브라질에 1:2. 그래도 경기장 청소는 잊지 않았다."),
(19,"스위스","Switzerland","ch","r32","B조 1위","B조 1위로 캐나다 제침. 32강 알제리."),
(20,"이란","Iran","ir","groupout","G조 3위","G조 3위, 3무로 탈락. 본선 최고 랭킹 탈락팀 2위."),
(21,"덴마크","Denmark","dk","noqual","미진출","랭킹 21위인데 예선 탈락. 유럽 예선의 잔혹함."),
(22,"튀르키예","Türkiye","tr","groupout","D조 4위","D조 4위 탈락. 그래도 마지막날 미국 잡은 게 위안."),
(23,"에콰도르","Ecuador","ec","r32","E조 3위","E조 3위로 통과. 독일을 2:1로 잡은 주인공. 32강 멕시코."),
(24,"오스트리아","Austria","at","r32","J조 2위","J조 2위. 알제리와 3:3 난타전 끝 생존. 32강 스페인."),
(25,"대한민국","South Korea","kr","groupout","A조 3위","A조 3위로 탈락. 멕시코·남아공에 밀렸다. 아쉬운 3위그룹 10위."),
(26,"나이지리아","Nigeria","ng","noqual","미진출","아프리카 강호지만 이번엔 본선 미진출."),
(27,"호주","Australia","au","r32","D조 2위","D조 2위로 토너먼트 무대. 32강 이집트."),
(28,"알제리","Algeria","dz","r32","J조 3위","J조 3위 와일드카드로 생존. 32강 스위스."),
(29,"이집트","Egypt","eg","r32","G조 2위","살라의 이집트. G조 2위. 32강 호주."),
(30,"캐나다","Canada","ca","r16","B조 2위","공동 개최국. 사상 첫 토너먼트 승리(남아공 1:0)로 16강. 대회 첫 진출 확정국."),
(31,"노르웨이","Norway","no","r32","I조 2위","홀란드의 첫 월드컵. I조 2위. 32강 코트디부아르."),
(32,"우크라이나","Ukraine","ua","noqual","미진출","랭킹 32위지만 본선 미진출."),
(33,"코트디부아르","Ivory Coast","ci","r32","E조 2위","E조 2위로 깜짝 통과. 32강 노르웨이."),
(34,"파나마","Panama","pa","groupout","L조 4위","L조 4위, 3패 무득점 탈락."),
(35,"러시아","Russia","ru","noqual","미진출","출전 정지로 예선부터 불참. 랭킹에만 남아 있다."),
(36,"폴란드","Poland","pl","noqual","미진출","레반도프스키도 본선行 실패."),
(37,"웨일스","Wales","gb-wls","noqual","미진출","본선 미진출."),
(38,"스웨덴","Sweden","se","r32","F조 3위","F조 3위 와일드카드. 32강서 프랑스라는 험로."),
(39,"헝가리","Hungary","hu","noqual","미진출","본선 미진출."),
(40,"체코","Czechia","cz","groupout","A조 4위","A조 4위 탈락. 한국에 1:2 패가 뼈아팠다."),
(41,"파라과이","Paraguay","py","r32","D조 3위","D조 3위 와일드카드. 32강 독일."),
(42,"스코틀랜드","Scotland","gb-sct","groupout","C조 3위","C조 3위로 또 좌절. 3위그룹 11위로 탈락."),
(43,"세르비아","Serbia","rs","noqual","미진출","본선 미진출."),
(44,"카메룬","Cameroon","cm","noqual","미진출","본선 미진출."),
(45,"튀니지","Tunisia","tn","groupout","F조 4위","F조 4위, 3패 -10 탈락. 대회 중 감독 경질."),
(46,"콩고DR","DR Congo","cd","r32","K조 3위","K조 3위로 와일드카드 1위. 32강 잉글랜드."),
(47,"슬로바키아","Slovakia","sk","noqual","미진출","본선 미진출."),
(48,"그리스","Greece","gr","noqual","미진출","본선 미진출."),
(49,"베네수엘라","Venezuela","ve","noqual","미진출","본선 미진출."),
(50,"우즈베키스탄","Uzbekistan","uz","groupout","K조 4위","K조 4위, 첫 월드컵서 3패 탈락."),
(51,"칠레","Chile","cl","noqual","미진출","본선 미진출."),
(52,"페루","Peru","pe","noqual","미진출","본선 미진출."),
(53,"코스타리카","Costa Rica","cr","noqual","미진출","본선 미진출."),
(54,"루마니아","Romania","ro","noqual","미진출","본선 미진출."),
(55,"말리","Mali","ml","noqual","미진출","본선 미진출."),
(56,"카타르","Qatar","qa","groupout","B조 4위","직전 개최국. B조 4위로 탈락."),
(57,"이라크","Iraq","iq","groupout","I조 4위","I조 4위, 세네갈에 0:5 등 3패 탈락."),
(58,"아일랜드","Ireland","ie","noqual","미진출","본선 미진출."),
(59,"슬로베니아","Slovenia","si","noqual","미진출","본선 미진출."),
(60,"남아프리카공화국","South Africa","za","r32out","A조 2위","A조 2위 깜짝 진출했으나 32강서 캐나다에 0:1 탈락."),
(61,"사우디아라비아","Saudi Arabia","sa","groupout","H조 4위","H조 4위 탈락."),
(62,"부르키나파소","Burkina Faso","bf","noqual","미진출","본선 미진출."),
(63,"요르단","Jordan","jo","groupout","J조 4위","첫 월드컵서 J조 4위 3패 탈락. 아르헨티나에 1:3."),
(64,"보스니아 헤르체고비나","Bosnia & Herzegovina","ba","r32","B조 3위","B조 3위 와일드카드. 32강 미국."),
]
TAG={"r16":("16강 진출","t-adv","r16"),"r32":("32강 생존","t-live","r32"),
 "r32out":("32강 OUT","t-out","r32out"),"groupout":("조별 OUT","t-out","groupout"),
 "noqual":("미진출","t-no","noqual")}

def m(a,b,date,res=None,win=None):
    return dict(a=a,b=b,date=date,res=res,win=win)
TIES_L=[
 (m(("남아공","za"),("캐나다","ca"),"",("0","1"),"b"), m(("네덜란드","nl"),("모로코","ma"),"6/29"), ("캐나다","ca")),
 (m(("독일","de"),("파라과이","py"),"6/29"), m(("프랑스","fr"),("스웨덴","se"),"6/30"), None),
 (m(("브라질","br"),("일본","jp"),"",("2","1"),"a"), m(("코트디부아르","ci"),("노르웨이","no"),"6/30"), ("브라질","br")),
 (m(("멕시코","mx"),("에콰도르","ec"),"6/30"), m(("잉글랜드","gb-eng"),("콩고DR","cd"),"7/1"), None),
]
TIES_R=[
 (m(("미국","us"),("보스니아","ba"),"7/1"), m(("벨기에","be"),("세네갈","sn"),"7/1"), None),
 (m(("포르투갈","pt"),("크로아티아","hr"),"7/2"), m(("스페인","es"),("오스트리아","at"),"7/2"), None),
 (m(("스위스","ch"),("알제리","dz"),"7/2"), m(("콜롬비아","co"),("가나","gh"),"7/3"), None),
 (m(("아르헨티나","ar"),("카보베르데","cv"),"7/3"), m(("호주","au"),("이집트","eg"),"7/3"), None),
]

cup='<svg class="cup" viewBox="0 0 64 74"><g stroke=""><path d="M16 6 H48 V22 A16 16 0 0 1 16 22 Z"/><path d="M16 12 H6 a8 8 0 0 0 8 10"/><path d="M48 12 H58 a8 8 0 0 1 -8 10"/><path d="M32 38 V52"/><path d="M22 66 H42 V70 H22 Z"/><path d="M26 52 H38 L40 66 H24 Z"/></g></svg>'

def mcard(mm):
    done=mm["res"] is not None
    sa=mm["res"][0] if done else ""; sb=mm["res"][1] if done else ""
    ca="w" if mm["win"]=="a" else("l" if mm["win"]=="b" else "")
    cb="w" if mm["win"]=="b" else("l" if mm["win"]=="a" else "")
    meta=f'<div class="mmeta r">RESULT</div>' if done else f'<div class="mmeta">{mm["date"]} 예정</div>'
    return f"""<div class="mt {'done' if done else ''}">
 <div class="mtr {ca}">{flag(mm['a'][1],mm['a'][0],'')}<span class="nm">{html.escape(mm['a'][0])}</span><span class="sc">{sa}</span></div>
 <div class="mtr {cb}">{flag(mm['b'][1],mm['b'][0],'')}<span class="nm">{html.escape(mm['b'][0])}</span><span class="sc">{sb}</span></div>
 {meta}</div>"""


# ===================== 자동 갱신 로직 =====================
API_MATCHES = "https://api.football-data.org/v4/competitions/WC/matches"
OVERRIDE = {"USA": "United States", "DR Congo": "Congo DR",
            "Bosnia & Herzegovina": "Bosnia-Herzegovina", "Türkiye": "Turkey"}
EXTRA_ISO = {"gh": "Ghana", "cv": "Cape Verde Islands", "ht": "Haiti", "cw": "Curaçao", "nz": "New Zealand"}
EXTRA_KO = {"gh": "가나", "cv": "카보베르데", "ht": "아이티", "cw": "퀴라소", "nz": "뉴질랜드"}
STAGE_KO = {"LAST_32": "32강", "LAST_16": "16강", "QUARTER_FINALS": "8강",
            "SEMI_FINALS": "4강", "THIRD_PLACE": "3·4위전", "FINAL": "결승", "GROUP_STAGE": "조별리그"}
KST = datetime.timezone(datetime.timedelta(hours=9))
NOW = datetime.datetime.now(KST)          # main에서 다시 설정
LIVE_STATUS = ("IN_PLAY", "PAUSED")


def to_kst(x):
    return datetime.datetime.fromisoformat(x["utcDate"].replace("Z", "+00:00")).astimezone(KST)


# ---- API-FOOTBALL 라이브 (경기중 스코어/상태) ----
LIVE_SCORES = {}    # {frozenset({iso_h, iso_a}): {"gh","ga","status","elapsed","home"}}  main에서 채움
ISO2KO = {}         # {iso: 한글명}  main에서 채움
ID2ISO = {}         # {football-data team id: iso}  main에서 채움
AF_URL = "https://v3.football.api-sports.io/fixtures?live=all"
AF_LIVE = {"1H", "2H", "HT", "ET", "BT", "P", "SUSP", "INT", "LIVE"}
AF_ALIAS = {
    "usa": "us", "unitedstates": "us", "unitedstatesofamerica": "us",
    "southkorea": "kr", "korearepublic": "kr", "republicofkorea": "kr", "korea": "kr",
    "czechrepublic": "cz", "czechia": "cz",
    "drcongo": "cd", "congodr": "cd", "democraticrepublicofthecongo": "cd", "democraticrepublicofcongo": "cd",
    "ivorycoast": "ci", "cotedivoire": "ci",
    "capeverde": "cv", "caboverde": "cv", "capeverdeislands": "cv",
    "iran": "ir", "iranislamicrepublic": "ir",
    "bosniaandherzegovina": "ba", "bosniaherzegovina": "ba", "bosnia": "ba",
    "turkey": "tr", "turkiye": "tr",
}


def _afnorm(s):
    return re.sub(r"[^a-z]", "", (s or "").lower())


def _af_iso(name, en2iso):
    n = _afnorm(name)
    if n in en2iso:
        return en2iso[n]
    return AF_ALIAS.get(n)


def fetch_af_live():
    """API-FOOTBALL 라이브 경기. 키 없으면 None(라이브 생략). --af-local FILE 로 테스트."""
    if "--af-local" in sys.argv:
        return json.load(open(sys.argv[sys.argv.index("--af-local") + 1], encoding="utf-8"))
    key = os.environ.get("APIFOOTBALL_KEY")
    if not key:
        return None
    req = urllib.request.Request(AF_URL, headers={"x-apisports-key": key})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def should_poll_live(timed):
    """경기 시간대인가: 킥오프 15분 전 ~ 150분 후 사이의 경기가 있으면 True (무료 한도 절약)."""
    for x in timed:
        dt = (to_kst(x) - NOW).total_seconds() / 60.0
        if -150 <= dt <= 15:
            return True
    return False


def compute_live_scores(af, en2iso):
    out = {}
    if not af:
        return out
    for f in af.get("response", []):
        try:
            st = f["fixture"]["status"]["short"]
            if st not in AF_LIVE:
                continue
            hi = _af_iso(f["teams"]["home"]["name"], en2iso)
            ai = _af_iso(f["teams"]["away"]["name"], en2iso)
            if not hi or not ai:
                continue
            out[frozenset({hi, ai})] = {
                "gh": f["goals"]["home"], "ga": f["goals"]["away"],
                "status": st, "elapsed": f["fixture"]["status"].get("elapsed"), "home": hi,
            }
        except Exception:
            continue
    return out


def fetch_matches():
    if "--local" in sys.argv:
        d = sys.argv[sys.argv.index("--local") + 1]
        with open(os.path.join(d, "wc_matches.json"), encoding="utf-8") as f:
            return json.load(f)["matches"]
    key = os.environ.get("FOOTBALL_DATA_KEY")
    if not key:
        sys.exit("FOOTBALL_DATA_KEY 환경변수가 없습니다.")
    req = urllib.request.Request(API_MATCHES, headers={"X-Auth-Token": key})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())["matches"]


def api_team_index(matches):
    t = {}
    for x in matches:
        for s in ("homeTeam", "awayTeam"):
            o = x[s]
            if o.get("id"):
                t[o["id"]] = {"name": o["name"], "short": o.get("shortName")}
    return t


def build_iso2id(api):
    name2id = {v["name"]: k for k, v in api.items()}
    short2id = {v["short"]: k for k, v in api.items() if v.get("short")}

    def fid(en):
        en = OVERRIDE.get(en, en)
        return name2id.get(en) or short2id.get(en)

    iso2id = {}
    for rank, ko, en, iso, st, grp, note in R:
        if st == "noqual":
            continue
        i = fid(en)
        if i:
            iso2id[iso] = i
    for iso, nm in EXTRA_ISO.items():
        if nm in name2id:
            iso2id[iso] = name2id[nm]
    return iso2id


def winner(x):
    s = x["score"]
    w = s.get("winner")
    if w == "HOME_TEAM":
        return "home"
    if w == "AWAY_TEAM":
        return "away"
    pen = s.get("penalties") or {}
    if pen.get("home") is not None and pen["home"] != pen["away"]:
        return "home" if pen["home"] > pen["away"] else "away"
    ft = s["fullTime"]
    if ft["home"] is not None and ft["home"] != ft["away"]:
        return "home" if ft["home"] > ft["away"] else "away"
    return None


def compute(matches, iso2id):
    id2iso = {v: k for k, v in iso2id.items()}
    status = {}            # id -> r16 / r32 / r32out / groupout
    r32_ids = set()
    r32_by_pair = {}       # frozenset(ids) -> match
    last16_done = False
    for x in matches:
        st = x["stage"]
        if st == "LAST_16" and x["status"] == "FINISHED":
            last16_done = True
        if st != "LAST_32":
            continue
        h = x["homeTeam"].get("id")
        a = x["awayTeam"].get("id")
        if h:
            r32_ids.add(h)
        if a:
            r32_ids.add(a)
        if h and a:
            r32_by_pair[frozenset((h, a))] = x
        if x["status"] == "FINISHED":
            w = winner(x)
            if w == "home":
                status[h] = "r16"
                status[a] = "r32out"
            elif w == "away":
                status[a] = "r16"
                status[h] = "r32out"
        else:
            status.setdefault(h, "r32")
            status.setdefault(a, "r32")
    wc_ids = set()
    for x in matches:
        if x["stage"] == "GROUP_STAGE":
            for s in ("homeTeam", "awayTeam"):
                if x[s].get("id"):
                    wc_ids.add(x[s]["id"])
    for tid in wc_ids:
        if tid not in r32_ids:
            status.setdefault(tid, "groupout")
    status_iso = {id2iso[i]: stt for i, stt in status.items() if i in id2iso}
    r32_pending = any(x["stage"] == "LAST_32" and x["status"] != "FINISHED" for x in matches)
    stage = "16강 진행" if last16_done else ("32강 진행" if r32_pending else "16강 대기")
    return status_iso, r32_by_pair, stage


# ---------- 영역 렌더 (상태 반영) ----------
def render_rank(status_iso):
    out = ""
    for rank, ko, en, iso, st0, grp, note in R:
        st = status_iso.get(iso, st0)
        lab, tc, gk = TAG[st]
        alive = "alive" if st in ("r16", "r32") else ("out" if st in ("r32out", "groupout") else "noqual")
        top = " top" if rank <= 3 else ""
        out += f'''<div class="srow{top}" data-g="{gk}" data-f="{alive}">
 <div class="srk">{rank}</div>{flag(iso, ko)}
 <div class="sname"><span class="ko">{html.escape(ko)}</span><span class="en">{html.escape(en)} · {grp}</span></div>
 <div class="tag {tc}">{lab}</div>
 <div class="snote">{html.escape(note)}</div></div>
'''
    return out


def _match_for(a_iso, b_iso, iso2id, by_pair):
    ia = iso2id.get(a_iso)
    ib = iso2id.get(b_iso)
    if ia is None or ib is None:
        return None, ia, ib
    return by_pair.get(frozenset((ia, ib))), ia, ib


def _card(a, b, sa, sb, ca, cb, meta):
    return (f'<div class="mt done">'
            f'<div class="mtr {ca}">{flag(a[1], a[0], "")}<span class="nm">{html.escape(a[0])}</span><span class="sc">{sa}</span></div>'
            f'<div class="mtr {cb}">{flag(b[1], b[0], "")}<span class="nm">{html.escape(b[0])}</span><span class="sc">{sb}</span></div>'
            f'{meta}</div>')


def render_mcard(a, b, date, iso2id, by_pair):
    ls = LIVE_SCORES.get(frozenset({a[1], b[1]}))
    if ls:
        sa, sb = (ls["gh"], ls["ga"]) if a[1] == ls["home"] else (ls["ga"], ls["gh"])
        sa = "" if sa is None else sa
        sb = "" if sb is None else sb
        el = ls.get("elapsed")
        meta = f'<div class="mmeta live">● LIVE {el}\'</div>' if el else '<div class="mmeta live">● LIVE</div>'
        return (f'<div class="mt live">'
                f'<div class="mtr ">{flag(a[1], a[0], "")}<span class="nm">{html.escape(a[0])}</span><span class="sc">{sa}</span></div>'
                f'<div class="mtr ">{flag(b[1], b[0], "")}<span class="nm">{html.escape(b[0])}</span><span class="sc">{sb}</span></div>'
                f'{meta}</div>')
    x, ia, ib = _match_for(a[1], b[1], iso2id, by_pair)
    if not x or x["status"] != "FINISHED":
        live = bool(x) and x["status"] in LIVE_STATUS
        today = bool(x) and to_kst(x).date() == NOW.date() and not live
        cls = "live" if live else ("today" if today else "")
        sa = sb = ""
        if live:
            ft = x["score"]["fullTime"]
            if ft.get("home") is not None:
                sa, sb = (ft["home"], ft["away"]) if x["homeTeam"]["id"] == ia else (ft["away"], ft["home"])
            meta = '<div class="mmeta live">● LIVE</div>'
        elif today:
            meta = f'<div class="mmeta today">오늘 {to_kst(x).strftime("%H:%M")}</div>'
        elif x:
            meta = f'<div class="mmeta">{to_kst(x).strftime("%m/%d %H:%M")}</div>'
        else:
            meta = f'<div class="mmeta">{date} 예정</div>'
        return (f'<div class="mt {cls}">'
                f'<div class="mtr ">{flag(a[1], a[0], "")}<span class="nm">{html.escape(a[0])}</span><span class="sc">{sa}</span></div>'
                f'<div class="mtr ">{flag(b[1], b[0], "")}<span class="nm">{html.escape(b[0])}</span><span class="sc">{sb}</span></div>'
                f'{meta}</div>')
    sc = x["score"]
    pso = sc.get("duration") == "PENALTY_SHOOTOUT"
    base = (sc.get("regularTime") or sc["fullTime"]) if pso else sc["fullTime"]
    pk = sc["fullTime"] if pso else None     # 이 데이터셋에서 PSO 최종 합계는 fullTime에 들어옴
    home_is_a = x["homeTeam"]["id"] == ia
    sa, sb = (base["home"], base["away"]) if home_is_a else (base["away"], base["home"])
    w = winner(x)
    wid = x["homeTeam"]["id"] if w == "home" else (x["awayTeam"]["id"] if w == "away" else None)
    ca = "w" if wid == ia else ("l" if wid == ib else "")
    cb = "w" if wid == ib else ("l" if wid == ia else "")
    if pk:
        pka, pkb = (pk["home"], pk["away"]) if home_is_a else (pk["away"], pk["home"])
        meta = f'<div class="mmeta r">승부차기 {pka}-{pkb}</div>'
    else:
        meta = '<div class="mmeta r">RESULT</div>'
    return _card(a, b, sa, sb, ca, cb, meta)


def _advancers(t, iso2id, by_pair):
    adv = []
    for mm in (t[0], t[1]):
        x, ia, ib = _match_for(mm["a"][1], mm["b"][1], iso2id, by_pair)
        if x and x["status"] == "FINISHED":
            w = winner(x)
            wid = x["homeTeam"]["id"] if w == "home" else (x["awayTeam"]["id"] if w == "away" else None)
            if wid == ia:
                adv.append(mm["a"])
            elif wid == ib:
                adv.append(mm["b"])
    return adv


def slot_multi(advs):
    if not advs:
        return '<div class="slot"><span class="l">16강</span><span class="w">승자 대기</span></div>'
    inner = "".join(f'{flag(a[1], a[0], "")}{html.escape(a[0])}' for a in advs)
    return f'<div class="slot live"><span class="l">16강</span><span class="ad">{inner}</span></div>'


def render_tie(t, side, iso2id, by_pair):
    m1, m2, _ = t
    cards = render_mcard(m1["a"], m1["b"], m1["date"], iso2id, by_pair) + \
        render_mcard(m2["a"], m2["b"], m2["date"], iso2id, by_pair)
    return (f'<div class="tie {side}"><div class="tie-m">{cards}</div>'
            f'<div class="jn"></div>{slot_multi(_advancers(t, iso2id, by_pair))}</div>')


def render_bcenter(r16_kos):
    if not r16_kos:
        q = "미정"
    elif len(r16_kos) <= 8:
        q = " · ".join(ko for ko, iso in r16_kos)
    else:
        q = f"{len(r16_kos)}개국"
    return (f'<div class="bcenter">{cup}<div class="cbox"><div class="t">Champion</div>\n'
            f'<div class="d">8강 7/9~11<br>4강 7/14~15<br>결승 7/19<br>METLIFE</div>\n'
            f'<div class="q">16강 확정<br>{html.escape(q)}</div></div></div>')


def render_bracket(iso2id, by_pair, r16_kos):
    L = "".join(render_tie(t, "", iso2id, by_pair) for t in TIES_L)
    Rr = "".join(render_tie(t, "r", iso2id, by_pair) for t in TIES_R)
    return f'<div class="bcol l">{L}</div>{render_bcenter(r16_kos)}<div class="bcol rr">{Rr}</div>'


def render_ticks(status_iso):
    top64 = [iso for (_, _, _, iso, st, _, _) in R if st != "noqual"]
    alive = sum(1 for iso in top64 if status_iso.get(iso) in ("r16", "r32"))
    out = sum(1 for iso in top64 if status_iso.get(iso) in ("r32out", "groupout"))
    return (f'<div class="tick y"><div class="n">64</div><div class="l">Ranked</div></div>'
            f'<div class="tick g"><div class="n">43</div><div class="l">본선 진출</div></div>'
            f'<div class="tick"><div class="n" style="color:var(--acc)">{alive}</div><div class="l">생존</div></div>'
            f'<div class="tick r"><div class="n">{out}</div><div class="l">탈락</div></div>'
            f'<div class="tick m"><div class="n">21</div><div class="l">미진출</div></div>')


def render_qf(stage, r16_kos):
    n = len(r16_kos)
    v16 = "미정" if n == 0 else (" · ".join(ko for ko, iso in r16_kos) if n <= 6 else f"{n}개국")
    cells = [("개최", "미국·캐나다·멕시코"), ("기간", "6.11 ~ 7.19"), ("참가", "48개국"),
             ("현재 단계", stage), ("FIFA 1위", "아르헨티나"), ("16강 확정", v16)]
    return "".join(
        f'<div class="c"><div class="k">{html.escape(k)}</div><div class="v">{html.escape(v)}</div></div>'
        for k, v in cells)


def render_updated():
    kst = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    return f'최종 업데이트 {kst:%Y-%m-%d %H:%M} KST · FIFA 랭킹 기준일 2026-06-11(공식, 대회 중 고정)'


# ---------- index.html 영역 교체 ----------
def replace_inner(page, anchor, new_inner):
    i = page.index(anchor)
    open_end = page.index(">", i) + 1
    depth, j = 1, open_end
    while depth > 0:
        nd = page.find("<div", j)
        nc = page.find("</div>", j)
        if nc == -1:
            raise ValueError("closing </div> not found for " + anchor)
        if nd != -1 and nd < nc:
            depth += 1
            j = nd + 4
        else:
            depth -= 1
            j = nc + 6
    return page[:open_end] + new_inner + page[j - 6:]


def schedule_info(matches):
    live = [x for x in matches if x["status"] in LIVE_STATUS]
    timed = sorted((x for x in matches if x["status"] in ("TIMED", "SCHEDULED")),
                   key=lambda x: x["utcDate"])
    today = [x for x in timed if to_kst(x).date() == NOW.date()]
    return live, today, timed


def _team_ko(o, id2ko):
    i = o.get("id")
    if i in id2ko:
        return id2ko[i]
    return o.get("shortName") or o.get("name") or "미정"


def _match_label(x, id2ko):
    return _team_ko(x["homeTeam"], id2ko) + " vs " + _team_ko(x["awayTeam"], id2ko)


_WD = ["월", "화", "수", "목", "금", "토", "일"]


def render_dock(live, today, timed, id2ko):
    if LIVE_SCORES:
        key, ls = next(iter(LIVE_SCORES.items()))
        isos = list(key)
        hi = ls["home"]
        ai = isos[0] if isos[1] == hi else isos[1]
        h = ISO2KO.get(hi, hi)
        aw = ISO2KO.get(ai, ai)
        gh = "" if ls["gh"] is None else ls["gh"]
        ga = "" if ls["ga"] is None else ls["ga"]
        el = ls.get("elapsed")
        tail = f" · {el}'" if el else ""
        badge = f'<span class="db live">● LIVE · {html.escape(h)} {gh}-{ga} {html.escape(aw)}{tail}</span>'
    else:
        today_left = [x for x in today if x["status"] in ("TIMED", "SCHEDULED")]
        if today_left:
            nx = today_left[0]
            badge = (f'<span class="db soon">오늘 {len(today_left)}경기 · 다음 '
                     f'{to_kst(nx).strftime("%H:%M")} {html.escape(_match_label(nx, id2ko))}</span>')
        elif timed:
            nx = timed[0]
            badge = (f'<span class="db soon">다음 {to_kst(nx).strftime("%m/%d %H:%M")} '
                     f'{html.escape(_match_label(nx, id2ko))}</span>')
        else:
            badge = '<span class="db">대회 종료</span>'
    iso = NOW.astimezone(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    upd = (f'<span class="db up"><span class="ago" data-iso="{iso}">방금</span> 갱신 · '
           f'{NOW.strftime("%H:%M")} KST · 경기 중 수 분마다 자동</span>')
    views = '<span class="db vw">조회수 <b id="viewsN">···</b></span>'
    return badge + upd + views


def render_sched(live, timed, id2ko):
    rows = []
    live_keys = set(LIVE_SCORES.keys())
    # 라이브 경기 먼저 (스코어 포함)
    for key, ls in LIVE_SCORES.items():
        isos = list(key)
        hi = ls["home"]
        ai = isos[0] if isos[1] == hi else isos[1]
        h = ISO2KO.get(hi, hi)
        aw = ISO2KO.get(ai, ai)
        gh = "" if ls["gh"] is None else ls["gh"]
        ga = "" if ls["ga"] is None else ls["ga"]
        el = ls.get("elapsed")
        when = f"LIVE {el}'" if el else "LIVE"
        rows.append(f'<div class="sl live"><span class="sw">{when}</span><span class="sg">진행중</span>'
                    f'<span class="sm">{html.escape(h)} {gh}-{ga} {html.escape(aw)}</span></div>')
    # 예정/기타 (라이브 중인 경기는 제외)
    for x in (live + timed):
        if len(rows) >= 8:
            break
        pair = frozenset({ID2ISO.get(x["homeTeam"].get("id")), ID2ISO.get(x["awayTeam"].get("id"))})
        if pair in live_keys:
            continue
        t = to_kst(x)
        istoday = t.date() == NOW.date()
        cls = "today" if istoday else ""
        if istoday:
            when = f'오늘 {t.strftime("%H:%M")}'
        else:
            when = f'{t.strftime("%m/%d")}({_WD[t.weekday()]}) {t.strftime("%H:%M")}'
        rows.append(f'<div class="sl {cls}"><span class="sw">{when}</span>'
                    f'<span class="sg">{STAGE_KO.get(x["stage"], "")}</span>'
                    f'<span class="sm">{html.escape(_match_label(x, id2ko))}</span></div>')
    if not rows:
        rows.append('<div class="sl"><span class="sm">남은 경기가 없습니다.</span></div>')
    return "".join(rows)


def main():
    global NOW, LIVE_SCORES, ISO2KO, ID2ISO
    NOW = datetime.datetime.now(KST)
    here = os.path.dirname(os.path.abspath(__file__))
    matches = fetch_matches()
    api = api_team_index(matches)
    iso2id = build_iso2id(api)
    status_iso, by_pair, stage = compute(matches, iso2id)

    id2ko = {}
    for (_, ko, _, iso, _, _, _) in R:
        if iso in iso2id:
            id2ko[iso2id[iso]] = ko
    for iso, ko in EXTRA_KO.items():
        if iso in iso2id:
            id2ko[iso2id[iso]] = ko

    live, today, timed = schedule_info(matches)

    ISO2KO = {iso: ko for (_, ko, _, iso, _, _, _) in R}
    ISO2KO.update(EXTRA_KO)
    ID2ISO = {v: k for k, v in iso2id.items()}
    en2iso = {_afnorm(en): iso for (_, _, en, iso, _, _, _) in R}
    for iso, en in EXTRA_ISO.items():
        en2iso[_afnorm(en)] = iso

    # 경기 시간대일 때만 API-FOOTBALL 라이브 호출 (무료 100/day 한도 절약)
    if should_poll_live(timed) or "--af-local" in sys.argv:
        LIVE_SCORES = compute_live_scores(fetch_af_live(), en2iso)

    r_isos = {iso for (_, _, _, iso, _, _, _) in R}
    r16_kos = [(ko, iso) for (_, ko, _, iso, _, _, _) in R if status_iso.get(iso) == "r16"]
    for iso, stt in status_iso.items():
        if stt == "r16" and iso not in r_isos:
            r16_kos.append((EXTRA_KO.get(iso, iso), iso))

    path = os.path.join(here, "index.html")
    page = open(path, encoding="utf-8").read()
    page = replace_inner(page, 'id="sheet"', render_rank(status_iso))
    page = replace_inner(page, 'class="bk"', render_bracket(iso2id, by_pair, r16_kos))
    page = replace_inner(page, 'class="ticks"', render_ticks(status_iso))
    page = replace_inner(page, 'class="qf"', render_qf(stage, r16_kos))
    page = replace_inner(page, 'class="dock"', render_dock(live, today, timed, id2ko))
    page = replace_inner(page, 'class="sched"', render_sched(live, timed, id2ko))
    page = replace_inner(page, 'class="updated"', render_updated())
    open(path, "w", encoding="utf-8").write(page)

    from collections import Counter
    c = Counter(status_iso.values())
    print(f"OK · 16강 {c.get('r16', 0)} · 32강생존 {c.get('r32', 0)} · "
          f"32강탈락 {c.get('r32out', 0)} · stage {stage} · 오늘 {len(today)} · AF라이브 {len(LIVE_SCORES)}")
    print("16강 확정:", ", ".join(ko for ko, iso in r16_kos))


if __name__ == "__main__":
    main()
