<template>
	<div class="index">
		<div class="card">
			Loream Ipsum
		</div>
		<button class=" btn btn-warning ">Click Me</button>
	</div>
</template>

<script type="text/javascript">
	export default{
		name:'index',
		data(){
			return {

			}
		}
	}
</script>

<style type="text/css">
	.index{
		height: 40%;
		width: 50%;
		margin: 0 auto;
		top: 0;
	}
	.card{
		height: 100px;
		width: 150px;
		
		float: left;
		margin-right: 10px;
		/*border: 0.5px solid #000;
		background-color: #bbb;*/
		border-radius: .25rem !important;
		padding: 1rem !important;
		margin-bottom: 3rem !important;
		background-color: #bbb !important;
		box-shadow: 0 1rem 3rem rgba(0,0,0,.175) !important;
		
	}
</style>