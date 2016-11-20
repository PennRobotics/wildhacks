from clarifai.rest import ClarifaiApp
import sys

app = ClarifaiApp("6zulHxkvEFX0EPgMuGH7ebBblNdGdYlklFcMLAG_", "eKLLsf5GZ4aKvZEOlrRKKXlXTOaS4gpOMfVbK4G1", quiet=True)

try:
    filelist = [sys.argv[1]]
except:
    filelist = ["music/jpg/pachelbel_canon_d_major_duet.jpg", "music/jpg/jo_stafford_ill_never_smile_again.jpg", "music/rock/metallica_enter_sandman.jpg", "music/rap/dr_dre_kush.jpg"]

if 0:
    # import a few labeld images
    app.inputs.create_image_from_filename(filename="music/jpg/bach_jesu_joy_of_mans_desiring.jpg", concepts=["classical"], not_concepts=["jazz", "rap", "rock"], allow_duplicate_url=True)
    app.inputs.create_image_from_filename(filename="music/jpg/beethoven_duet_allegro_c_major.jpg", concepts=["classical"], not_concepts=["jazz", "rap", "rock"], allow_duplicate_url=True)
    app.inputs.create_image_from_filename(filename="music/jpg/rimsky_korsakov_scheherezade.jpg", concepts=["classical"], not_concepts=["jazz", "rap", "rock"], allow_duplicate_url=True)
    app.inputs.create_image_from_filename(filename="music/jpg/vivaldi_four_seasons_spring.jpg", concepts=["classical"], not_concepts=["jazz", "rap", "rock"], allow_duplicate_url=True)
    app.inputs.create_image_from_filename(filename="music/jpg/faure_pavane_op_50.jpg", concepts=["classical"], not_concepts=["jazz", "rap", "rock"], allow_duplicate_url=True)
    app.inputs.create_image_from_filename(filename="music/jpg/brahms_hungarian_dance.jpg", concepts=["classical"], not_concepts=["jazz", "rap", "rock"], allow_duplicate_url=True)

    app.inputs.create_image_from_filename(filename="music/jpg/berlin_cheek_to_cheek.jpg", concepts=["jazz"], not_concepts=["classical", "rap", "rock"], allow_duplicate_url=True)
    app.inputs.create_image_from_filename(filename="music/jpg/weill_mack_the_knife.jpg", concepts=["jazz"], not_concepts=["classical", "rap", "rock"], allow_duplicate_url=True)
    app.inputs.create_image_from_filename(filename="music/jpg/hudson_moon_glow.jpg", concepts=["jazz"], not_concepts=["classical", "rap", "rock"], allow_duplicate_url=True)
    app.inputs.create_image_from_filename(filename="music/jpg/gershwin_embraceable_you.jpg", concepts=["jazz"], not_concepts=["classical", "rap", "rock"], allow_duplicate_url=True)

    app.inputs.create_image_from_filename(filename="music/rap/drake_hotline_bling.jpg", concepts=["rap"], not_concepts=["rock", "jazz", "classical"], allow_duplicate_url=True)
    app.inputs.create_image_from_filename(filename="music/rap/lil_wayne_rich_as_fuck.jpg", concepts=["rap"], not_concepts=["rock", "jazz", "classical"], allow_duplicate_url=True)
    app.inputs.create_image_from_filename(filename="music/rap/madeintyo_i_want.jpg", concepts=["rap"], not_concepts=["rock", "jazz", "classical"], allow_duplicate_url=True)
    app.inputs.create_image_from_filename(filename="music/rap/wiz_khalifa_bake_sale.jpg", concepts=["rap"], not_concepts=["rock", "jazz", "classical"], allow_duplicate_url=True)
    app.inputs.create_image_from_filename(filename="music/rap/ll_cool_j_headsprung.jpg", concepts=["rap"], not_concepts=["rock", "jazz", "classical"], allow_duplicate_url=True)
    app.inputs.create_image_from_filename(filename="music/rap/missy_elliott_where_they_from.jpg", concepts=["rap"], not_concepts=["rock", "jazz", "classical"], allow_duplicate_url=True)

    app.inputs.create_image_from_filename(filename="music/rock/guns_n_roses_paradise_city.jpg", concepts=["rock"], not_concepts=["rap", "jazz", "classical"], allow_duplicate_url=True)
    app.inputs.create_image_from_filename(filename="music/rock/nirvana_smells_like_teen_spirit.jpg", concepts=["rock"], not_concepts=["rap", "jazz", "classical"], allow_duplicate_url=True)
    app.inputs.create_image_from_filename(filename="music/rock/three_doors_down_kryptonite.jpg", concepts=["rock"], not_concepts=["rap", "jazz", "classical"], allow_duplicate_url=True)
    app.inputs.create_image_from_filename(filename="music/rock/rick_astley_never_gonna_give_you_up.jpg", concepts=["rock"], not_concepts=["rap", "jazz", "classical"], allow_duplicate_url=True)
    app.inputs.create_image_from_filename(filename="music/rock/aha_take_on_me.jpg", concepts=["rock"], not_concepts=["rap", "jazz", "classical"], allow_duplicate_url=True)
    app.inputs.create_image_from_filename(filename="music/rock/europe_the_final_countdown.jpg", concepts=["rock"], not_concepts=["rap", "jazz", "classical"], allow_duplicate_url=True)
    app.inputs.create_image_from_filename(filename="music/rock/survivor_eye_of_the_tiger.jpg", concepts=["rock"], not_concepts=["rap", "jazz", "classical"], allow_duplicate_url=True)

    app.models.delete("music")
    model = app.models.create(model_id="music", concepts=["classical", "jazz", "rap", "rock"])
    model = model.train()

else:
    model = app.models.get(model_id="music")

print('----')
for file in filelist:
    print('Predicting ' + file)
    result = model.predict_by_filename(file)
    cat, p = zip(*[(i[u'id'], i[u'value']) for i in result[u'outputs'][0][u'data'][u'concepts']])
    print(cat)
    print(p)
    print('----')
