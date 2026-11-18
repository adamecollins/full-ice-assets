from PIL import Image, ImageDraw, ImageFont
S=2; W,H=1200,630
INK=(16,33,46); BODY=(34,49,63); BLUE=(46,111,163); RED=(200,16,46); GRAY=(96,112,125); RULE=(217,226,233); FROST=(244,248,251)
im=Image.new("RGB",(W*S,H*S),(255,255,255)); d=ImageDraw.Draw(im)
L="/usr/share/fonts/truetype/liberation/"
serifB=lambda s:ImageFont.truetype(L+"LiberationSerif-Bold.ttf",s*S)
sans=lambda s:ImageFont.truetype(L+"LiberationSans-Regular.ttf",s*S)
sansB=lambda s:ImageFont.truetype(L+"LiberationSans-Bold.ttf",s*S)
P=lambda x,y:(x*S,y*S); M=70
def tribar(y):
    for i,c in enumerate([BLUE,RED,BLUE]): d.rectangle([0,(y+i*9)*S,W*S,(y+i*9+4)*S],fill=c)
def spaced(x,y,t,f,fill,sp):
    for ch in t: d.text(P(x,y),ch,font=f,fill=fill); x+=d.textlength(ch,font=f)/S+sp
tribar(0)
d.rectangle([P(M,62),P(M+34,65)],fill=RED)
spaced(M,76,"FULL ICE  ·  №14  ·  NOVEMBER 19, 2026",sansB(19),INK,2.5)
d.text(P(M,124),"The DL's first reported dates,",font=serifB(58),fill=INK)
d.text(P(M,194),"and when a player wants out.",font=serifB(58),fill=INK)
assert d.textlength("and when a player wants out.",font=serifB(58))/S < W-2*M
y0=306; d.rectangle([P(M,y0),P(W-M,y0+196)],fill=FROST); d.rectangle([P(M,y0),P(W-M,y0+1)],fill=RULE)
cols=[("Sept. 2027","first DL showcase","reported, Rochester"),("March 2028","DL championships","reported target week"),("About 70%","quit organized sport","by age 13, AAP, 2024"),("$0","back after Oct. 20","Milton, Ont., policy")]
cw=(W-2*M)/4
for i,(a,b,c) in enumerate(cols):
    x=M+i*cw+28
    if i: d.rectangle([P(M+i*cw,y0+28),P(M+i*cw+1,y0+172)],fill=RULE)
    d.text(P(x,y0+26),a,font=serifB(40),fill=RED if i==0 else INK); assert d.textlength(a,font=serifB(40))/S < cw-40,(a,)
    d.text(P(x,y0+92),b,font=sansB(21),fill=BODY)
    d.text(P(x,y0+120),c,font=sans(19),fill=GRAY)
    for t,f in ((b,sansB(21)),(c,sans(19))):
        assert d.textlength(t,font=f)/S < cw-40, (t,)
d.text(P(M,528),"Plus: a city rink in Los Angeles, rink netting, and a backyard rink.",font=sans(24),fill=BODY)
d.text(P(M,568),"Sources: Clanko Media, Nov. 18, 2026; American Academy of Pediatrics, 2024; Milton Minor Hockey refund policy, 2026-27",font=sans(16),fill=GRAY)
fw=d.textlength("fullicemedia.com",font=sansB(26))/S
d.text(P(W-M-fw,536),"fullicemedia.com",font=sansB(26),fill=BLUE)
tribar(H-22)
im.resize((W,H),Image.LANCZOS).save("fullice-014-share-1200x630.png"); print("ok")
