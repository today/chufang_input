'use strict';

/* Controllers */


var frtControllers = angular.module('frtControllers', []);

frtControllers.controller('indexCtrl', ['$scope', 
  function($scope, $http) {
    
       $scope.tempValue = 12;
 
  }]);

frtControllers.controller('input_1_Ctrl', ['$scope',
  function($scope, $http) {
    
  $scope.value = 12;
  $scope.new_or_old = "old";
  $scope.new_patient = "";
  $scope.show_new = true;
  $scope.show_old = false;
  $scope.show_next = true;

  // 第一次就诊的患者的图片：读入目录下全部文件，这个目录放全部 。
  var files = fs.readdirSync("./new_photos");
  var imgFiles = [];
  // 筛选出 jpg 文件
  files.forEach(function(fileName, index) {
    if( ".jpg" === path.extname(fileName) ){
      imgFiles.push(fileName);
    }
    //console.log( path.extname(fileName) );
  });
  $scope.new_filenames = imgFiles;

  // 复诊的患者的资料：读入json文件 。
  var patients_txt = fs.readFileSync("./data/patients.json");
  patients_json = JSON.parse(patients_txt);
  // 筛选出 复诊患者
  var patients_temp = [];
  patients_json.forEach(function(patient, index) {
    if( "n" === patient.flag_is_blank ){
      patients_temp.push(patient);
    }
    //console.log( patient.patient_id );
  });
  $scope.patient_infos = patients_temp;

  $scope.triggle_new = function(){
    $scope.new_or_old = "new";
    $scope.show_new = false;
    $scope.show_old = true;
    $scope.show_next = true;
  };
  $scope.triggle_old = function(){
    $scope.new_or_old = "old";
    $scope.show_new = true;
    $scope.show_old = false;
    $scope.show_next = true;
  };

  $scope.setPatientId = function( patient ){
    $scope.old_patient = patient.patient_id;
    $scope.show_next = false;
  };

  $scope.setPhotoName = function( imgname ){
    $scope.new_patient = imgname;
    $scope.show_next = false;
  };

  $scope.goInput = function(){
    // 先判断是复诊还是新患者
    if( 'new' === $scope.new_or_old ){
      // 新患者，先分配ID

      // 然后将图片文件名传给下一个画面
      
    }
    else if ('old' === $scope.new_or_old ){
      // 将id传给下一个画面
      var url_desc = 'input.html/' + $scope.old_patient;
      //alert(url_desc);
      
      redirectTo: url_desc
      
    }
    else{
      console.log( "Error!" );
      console.log( $scope.new_or_old );
    }
    
    window.location.href = "input.html";
  };
  
  $scope.testA = function() {
    console.log( JSON.stringify($scope.new_or_old) );

    console.log( JSON.stringify($scope.new_patient) );
  };
 
  }]);


