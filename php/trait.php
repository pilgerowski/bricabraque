<?php
	class OutraClasse {
		public $oi;

		public function __construct() {
			$this->oi = "Oi OutraClasse!";
		}

		public function digaOi() {
			echo $this->oi;
		}
	}

	trait ExemploDeTrait {
		public function digaOi() 
		{
			$this->oi = "Oi ExemploDeTrait!";
			$this->faleOi();
		}
	}

	trait OutroExemploDeTrait {

		public function faleOi() 
		{
			echo $this->oi;
		}
	}

	class Classe extends OutraClasse {

		use ExemploDeTrait, OutroExemploDeTrait;

		public function oi()
		{
			$this->digaOi();
		}
	}

	$classe = new Classe();
	echo $classe->oi;
	$classe->oi();
	echo "\n";
