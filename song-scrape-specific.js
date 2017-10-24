
var casper = require('casper').create({verbose: true , logLevel: "debug" });
var fs = require('fs');
var url = "https://ytmp3.cc/";
if(casper.cli.args.length === 0 ){
	casper.echo("usage: casperjs sample.js youtube-url song-name");
	casper.exit();
}else{
	var youtubeUrl = "" + casper.cli.get(0) + "";
	casper.start(url);

	casper.then(function(){
		this.fill('#converter > form', { 'video': youtubeUrl }, true);
	});
	casper.wait(2000);//this is probably what I was missing, 
					//a screen capture showed that I wasn't waiting long enough
	casper.then(function(){
		this.waitForSelector("#file", function(){
			var url = casper.getElementAttribute('#file','href');
			var mp3 = fs.absolute("Desktop/SongScrapeFolder/" + casper.cli.get(1) + ".mp3");
			casper.then(function() { this.download( url, mp3); });
		});
	});
	casper.run();
}
