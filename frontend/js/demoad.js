(function() {
    
    var filename = './css/demoad.css?' + new Date().getTime();
    var fileref = document.createElement("link");
    fileref.setAttribute("rel", "stylesheet");
    fileref.setAttribute("type", "text/css");
    fileref.setAttribute("href", filename);
    document.getElementsByTagName("head")[0].appendChild(fileref);

    let cdaSpots = ['ad1'];
    let cdaSpot = cdaSpots[Math.floor(Math.random() * cdaSpots.length)];

    switch (cdaSpot) {
        case "ad1":
            var cdaLink = 'https://ad.doubleclick.net/ddm/trackclk/N1224323.3091281BUYSELLADS/B29258209.358661418;dc_trk_aid=549462698;dc_trk_cid=186410004;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;ltd=';
            var cdaImg = 'https://tympanus.net/codrops/wp-content/banners/mailchimp_demo.png';
            var cdaImgAlt = 'Mailchimp';
            var cdaText = "Sign up for Mailchimp today.";
            break;
        case "ad2":
            var cdaLink = 'https://srv.buysellads.com/ads/long/x/T6PVCZS6TTTTTTFYUWWCVTTTTTTGJFQFKETTTTTTBT74O7TTTTTTTRPN22VNKKPKZHWWN73L2QQFEKPHVWSNAB77KWSE';
            var cdaImg = 'https://tympanus.net/codrops/wp-content/uploads/2023/04/Centra_sidebar_opt.png';
            var cdaImgAlt = 'Applitools Centra';
            var cdaText = "Connect Design and Development to Deliver Better Customer Experiences with Applitools Centra.";
            break;
        case "ad3":
            var cdaLink = 'https://ad.doubleclick.net/ddm/trackclk/N718679.452584BUYSELLADS.COM/B26953268.342937760;dc_trk_aid=534766646;dc_trk_cid=175795063;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;ltd=';
            var cdaImg = 'https://tympanus.net/codrops/wp-content/uploads/2022/08/SS.jpg';
            var cdaImgAlt = 'Squarespace';
            var cdaText = "Whatever your idea, you can sell it on Squarespace.";
            break;
        default:
            var cdaLink = 'https://www.elegantthemes.com/affiliates/idevaffiliate.php?id=17972_5_1_16';
            var cdaImg = 'https://tympanus.net/codrops/wp-content/banners/Divi_Carbon.jpg';
            var cdaImgAlt = 'Divi';
            var cdaText = "From our sponsor: Divi is more than just a WordPress theme, it's a completely new website building platform. Try it.";
    }
})();