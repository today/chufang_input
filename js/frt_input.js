fs = require('fs');

function getYMD( aDate ){
	var year = aDate.getFullYear();
	var month = aDate.getMonth()+1;
	var day = aDate.getDate();

	var strDate = "" + year + "-" + month + "-" + day;
	console.log(strDate);

	return strDate;

}

function getBookingFilename( aDate ){
	return 'data/booking_' + getYMD(aDate) + '.json' ;
}

// 读入指定日期的预约登记表
function getBooking( aDate ){
	var aJson = [];
	var strFilename = getBookingFilename(aDate) ;

	if(fs.existsSync( strFilename) ){
		var strBookingList = fs.readFileSync(strFilename);
		//console.log("getBooking(): " + strBookingList);
	    aJson = JSON.parse(strBookingList);
	}
	
	return aJson;

	
} 