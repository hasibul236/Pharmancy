<template>
  <div class="home">
  	<div class="container-fluid">
  		<div class="row">
  			
  		</div>
  		<div class="row">
  			<div class="col-md-4 shadowarea">
  				<div class="text-center" data-toggle="collapse" data-target="#academictiles" aria-expanded="false" aria-controls="academictiles">
  					<p class="header1">Academic <i class="fa fa-chevron-down arrowposition" aria-hidden="true"></i></p>
  				</div>
  				<div class="grid-container1 collapse multi-collapse" id="academictiles">
				  <div class="item1">
				  	<i class="fa fa-info-circle fa-2x text-center" aria-hidden="true"></i>
				  	<br>Admission
				  </div>
				  <div class="item1">
				  	<i class="fa fa-calendar fa-2x text-center" aria-hidden="true"></i><br>
				  	<span>Calender</span>
				  </div>
				  <div class="item3"><i class="fa fa-television fa-2x text-center" aria-hidden="true"></i>Chanakya</div>  
				  <div class="item4"><i class="fa fa-graduation-cap fa-2x text-center" aria-hidden="true"></i>Convocation</div>
				  <div class="item3"><i class="fa fa-home fa-2x text-center" aria-hidden="true"></i>Departments</div>
				  <div class="item6"><i class="fa fa-book fa-2x text-center" aria-hidden="true"></i><br>Documents</div>
				  <div class="item3"><i class="fa fa-pencil-square-o fa-2x text-center" aria-hidden="true"></i>Examinations</div>
				  <div class="item3"><i class="fa fa-file-word-o fa-2x text-center" aria-hidden="true"></i>Notices</div>
				  <div class="item1"><i class="fa fa-university fa-2x text-center" aria-hidden="true"></i>Registrations</div>
				  <div class="item6"><i class="fa fa-balance-scale fa-2x text-center" aria-hidden="true"></i><br>Regularations</div>
				</div>
  			</div>
  			<div class="col-md-4 shadowarea">
  				<div class="text-center"  data-toggle="collapse" data-target="#administrationtiles" aria-expanded="false" aria-controls="administrationtiles">
  					<p class="header2">Administration<i class="fa fa-chevron-down arrowposition" aria-hidden="true"></i></p>
  				</div>
  				<div class="grid-container2 collapse multi-collapse" id="administrationtiles">
				  <div class="item1">1</div>
				  <div class="item1">2</div>
				  <div class="item1">3</div>  
				  <div class="item1">4</div>
				  <div class="item1">5</div>
				  <div class="item1">6</div>
				</div>
  			</div>
  			<div class="col-md-4 shadowarea">
  				<div class="text-center"  data-toggle="collapse" data-target="#studentstiles" aria-expanded="false" aria-controls="studentstiles">
  					<p class="header3">Students<i class="fa fa-chevron-down arrowposition" aria-hidden="true"></i></p>
  				</div>
  				<div class="grid-container3 collapse multi-collapse" id="studentstiles">
				  <div class="item1">1</div>
				  <div class="item1">2</div>
				  <div class="item1">3</div>  
				  <div class="item1">4</div>
				  <div class="item1">5</div>
				  <div class="item1">6</div>
				</div>
  			</div>
  		</div>
  		<div class="row" style="margin-top: 10px;">
  			<div class="col-md-4 shadowarea">
  				<div class="text-center" data-toggle="collapse" data-target="#activitiestiles" aria-expanded="false" aria-controls="activitiestiles">
  					<p class="header4">Activities<i class="fa fa-chevron-down arrowposition" aria-hidden="true"></i></p>
  				</div>
  				<div class="grid-container4 collapse multi-collapse" id="activitiestiles">
				  <div class="item1">1</div>
				  <div class="item1">2</div>
				  <div class="item3">3</div>  
				  <div class="item4">4</div>
				  <div class="item3">5</div>
				  <div class="item6">6</div>
				</div>
  			</div>
  			<div class="col-md-4 shadowarea">
  				<div class="text-center"  data-toggle="collapse" data-target="#facilitiestiles" aria-expanded="false" aria-controls="facilitiestiles">
  					<p class="header5">Facilities<i class="fa fa-chevron-down arrowposition" aria-hidden="true"></i></p>
  				</div>
  				<div class="grid-container5 collapse multi-collapse" id="facilitiestiles">
				  <div class="item1">1</div>
				  <div class="item1">2</div>
				  <div class="item3">3</div>  
				  <div class="item4">4</div>
				</div>
  			</div>
  			
  			<div class="col-md-4 shadowarea">
  				<div class="text-center"  data-toggle="collapse" data-target="#informationstiles" aria-expanded="false" aria-controls="informationstiles">
  					<p class="header6">Informations<i class="fa fa-chevron-down arrowposition" aria-hidden="true"></i></p>
  				</div>
  				<div class="grid-container6 collapse multi-collapse" id="informationstiles">
				  <div class="item1">1</div>
				  <div class="item1">2</div>
				  <div class="item3">3</div>  
				  <div class="item4">4</div>
				</div>
  			</div>
  		</div>
  		<div v-for="customer in customers"> <p>{{ customer.name }}</p></div>
  	</div>
  </div>
</template>

<script>
	import axios from 'axios'
export default {
  name: 'Home',
  data () {
  	return {
  		customers:{},
     
    }

  },
  created() {
    axios.get('http://127.0.0.1:8005/superuser/supplier/')
    	.then(response =>response.json())
    	.then((data)=>{
    	this.customers=data;
    })
    }
}
</script>
<style type="text/css">
	body{
		background-color: #2196F3;
	}
	.grid-container {
	  display: grid;
	  grid-template-columns: auto auto auto auto;
	  grid-gap: 5px;
	  /*background-color: #2196F3;*/
	  background: linear-gradient(90deg,#4a148c,#7e57c2);
	  padding: 5px;
	  grid-row-gap: 5px;
	  grid-column-gap: 5px;
	  margin-top: -10px;

	}
	.grid-container1 {
	  display: grid;
	  grid-template-columns: auto auto auto auto;
	  grid-gap: 5px;
	  /*background-color: #2196F3;*/
	  background: linear-gradient(90deg,#4a148c,#7e57c2);
	  padding: 5px;
	  grid-row-gap: 5px;
	  grid-column-gap: 5px;
	  margin-top: -10px;

	}
	.grid-container2 {
	  display: grid;
	  grid-template-columns: auto auto auto auto;
	  grid-gap: 5px;
	  /*background-color: #2196F3;*/
	  background: linear-gradient(90deg,#b71c1c,#f44336);
	  padding: 5px;
	  grid-row-gap: 5px;
	  grid-column-gap: 5px;
	  margin-top: -10px;

	}
	.grid-container3 {
	  display: grid;
	  grid-template-columns: auto auto auto auto;
	  grid-gap: 5px;
	  /*background-color: #2196F3;*/
	  background: linear-gradient(90deg,#000,#424242);
	  padding: 5px;
	  grid-row-gap: 5px;
	  grid-column-gap: 5px;
	  margin-top: -10px;

	}
	.grid-container4 {
	  display: grid;
	  grid-template-columns: auto auto auto auto;
	  grid-gap: 5px;
	  /*background-color: #2196F3;*/
	  background: linear-gradient(90deg,#006064,#0097a7);
	  padding: 5px;
	  grid-row-gap: 5px;
	  grid-column-gap: 5px;
	  margin-top: -10px;

	}
	.grid-container5 {
	  display: grid;
	  grid-template-columns: auto auto auto auto;
	  grid-gap: 5px;
	  /*background-color: #2196F3;*/
	  background: linear-gradient(90deg,#880e4f,#d81b60);
	  padding: 5px;
	  grid-row-gap: 5px;
	  grid-column-gap: 5px;
	  margin-top: -10px;

	}
	.grid-container6 {
	  display: grid;
	  grid-template-columns: auto auto auto auto;
	  grid-gap: 5px;
	  /*background-color: #2196F3;*/
	  background: linear-gradient(90deg,#002f6c,#01579b);
	  padding: 5px;
	  grid-row-gap: 5px;
	  grid-column-gap: 5px;
	  margin-top: -10px;

	}
	.grid-container1>div {
	  /*background-color: rgba(255, 255, 255, 0.8);*/
	  color: #FFF;
	  text-align: center;
	  padding:10px 0;
	  font-size: 20px;
	 cursor: pointer;
	 border:.5px solid #eee;
	 border-radius: 10px;
	}
	.grid-container2>div {
	  /*background-color: rgba(255, 255, 255, 0.8);*/
	  color: #FFF;
	  text-align: center;
	  padding:10px 0;
	  font-size: 20px;
	 cursor: pointer;
	 border:.5px solid #eee;
	 border-radius: 10px;
	}
	.grid-container3>div {
	  /*background-color: rgba(255, 255, 255, 0.8);*/
	  color: #FFF;
	  text-align: center;
	  padding:10px 0;
	  font-size: 20px;
	 cursor: pointer;
	 border:.5px solid #eee;
	 border-radius: 10px;
	}
	.grid-container4>div {
	  /*background-color: rgba(255, 255, 255, 0.8);*/
	  color: #FFF;
	  text-align: center;
	  padding:10px 0;
	  font-size: 20px;
	 cursor: pointer;
	 border:.5px solid #eee;
	 border-radius: 10px;
	}
	.grid-container5>div {
	  /*background-color: rgba(255, 255, 255, 0.8);*/
	  color: #FFF;
	  text-align: center;
	  padding:10px 0;
	  font-size: 20px;
	 cursor: pointer;
	 border:.5px solid #eee;
	 border-radius: 10px;
	}
	.grid-container6>div {
	  /*background-color: rgba(255, 255, 255, 0.8);*/
	  color: #FFF;
	  text-align: center;
	  padding:10px 0;
	  font-size: 20px;
	 cursor: pointer;
	 border:.5px solid #eee;
	 border-radius: 10px;
	}
	
	.grid-container1>div:hover{
		opacity: .3;
		color: red;
	}
	.grid-container2>div:hover{
		opacity: .3;
		color: red;
	}
	.grid-container3>div:hover{
		opacity: .3;
		color: red;
	}
	.grid-container4>div:hover{
		opacity: .3;
		color: red;
	}
	.grid-container5>div:hover{
		opacity: .3;
		color: red;
	}
	.grid-container6>div:hover{
		opacity: .3;
		color: red;
	}
	
	.item1 {
	  grid-column-end: span 2;
	}
	.item4 {
	  grid-column-end: span 2;
	}
	.item2 {
	  grid-row-end: span 2;
	}
	.item6{
		grid-column-end: span 4;
	}
	.header{
		height: 50px;
		width: 100%;
		padding:15px;
		background:linear-gradient(172deg,#bcb,#abc);
		font-size: 25px;

	}
	.header1{
		height: 50px;
		width: 100%;
		padding:15px;
		background: linear-gradient(90deg,#4a148c,#7e57c2);
		font-size: 25px;
		color: #FFF;
	}
	.header2{
		height: 50px;
		width: 100%;
		padding:15px;
		background: linear-gradient(90deg,#b71c1c,#f44336);
		font-size: 25px;
		color: #FFF;
	}
	.header3{
		height: 50px;
		width: 100%;
		padding:15px;
		background: linear-gradient(90deg,#000,#424242);
		font-size: 25px;
		color: #FFF;
	}
	.header4{
		height: 50px;
		width: 100%;
		padding:15px;
		background: linear-gradient(90deg,#006064,#0097a7);
		font-size: 25px;
		color: #FFF;
	}
	.header5{
		height: 50px;
		width: 100%;
		padding:15px;
		background: linear-gradient(90deg,#880e4f,#d81b60);
		font-size: 25px;
		color: #FFF;
	}
	.header6{
		height: 50px;
		width: 100%;
		padding:15px;
		background: linear-gradient(90deg,#002f6c,#01579b);
		font-size: 25px;
		color: #FFF;
	}
	
	.multi-collapse{
		/*background-color: #17a2b8;*/
	}
	.navstyle{
		background: linear-gradient(90deg,#004d40,#00695c)
	}
	i{
		padding-bottom: 3px;
	}
	.shadowarea{
		padding-right: 5px;
		box-shadow:0 2px 5px 0 rgba(0,0,0,.16),0 2px 10px 0 rgba(0,0,0,.12);
	}
	.arrowposition{
		float: right; text-align: right; margin-top: -5px;
	}
</style>