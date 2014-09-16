var fs = require('fs');
var mysql = require('mysql');

function getYMD( aDate ){
	var year = aDate.getFullYear();
	var month = aDate.getMonth()+1;
	var day = aDate.getDate();

	var strDate = "" + year + "-" + month + "-" + day;
	console.log(strDate);

	return strDate;

}

function isblank(strA){
	if(strA){
		if( "string" === typeof(strA) ){
			if( "" === strA.trim()){
				return true;
			}else{
				return false;
			}
		}else{
			return true;
		}
	}else{
		return true;
	}
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

function getJson2obj( strFilename ){
	var aJson = {};
	if(fs.existsSync( strFilename) ){
		var strBookingList = fs.readFileSync(strFilename);
	    aJson = JSON.parse(strBookingList);
	}
	return aJson;
} 

function save2Json( filename, obj){
	var jsonStr = JSON.stringify(obj);
	// Write a file:
	console.log( "jsonStr = ###" + jsonStr + "###" );
	fs.writeFileSync( filename , jsonStr);
}

function getSavedCases(){
	return getJson2obj('data/saved_cases.json');
}

