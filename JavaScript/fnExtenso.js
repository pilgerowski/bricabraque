/*
 * Função fnExtenso: retorna um dado número em formato extenso para pt-br
 *
 * Autor: Charles Roberto Pilger (charles@pilger.com.br)
 * 
 * Histórico:
 * 29/052017 - Criação da rotina
*/

var pNumeros = [ 
  1, 10, 99, 100, 111, 999, 1000, 9999, 10000, 99999, 100000, 999999, 1000000, 9999999, 10000000, 99999999, 
  100000000, 999999999, 1000000000, 9999999999, 10000000000, 99999999999, 100000000000, 999999999999, 
  1000000000000, 9999999999999, 10000000000000, 99999999999999, 100000000000000, 999999999999999, 1000000000000000
];

var nNumero = 0;
for(nNumero of pNumeros) {
  if( fnExtenso(nNumero) )
    console.log(nNumero + ' : ' + fnExtenso(nNumero));
  else 
    console.log('A função não oferece conversão para o valor ' + nNumero);
}

function fnExtenso(nNumero) {
  switch(nNumero) {
    case 0: return "zero";
    case 1: return 'um';
    case 2: return "dois";
    case 3: return "três";
    case 4: return "quatro";
    case 5: return "cinco";
    case 6: return "seis";
    case 7: return "sete";
    case 8: return "oito";
    case 9: return "nove";
    case 10: return "dez";
    case 11: return "onze";
    case 12: return "doze";
    case 13: return "treze";
    case 14: return "catorze";
    case 15: return "quinze";
    case 16: return "dezesseis";
    case 17: return "dezessete";
    case 18: return "dezoito";
    case 19: return "dezenove";
    case 20: return "vinte";
    case 30: return "trinta";
    case 40: return "quarenta";
    case 50: return "cinquenta";
    case 60: return "sessenta";
    case 70: return "setenta";
    case 80: return "oitenta";
    case 90: return "noventa";
    case 100: return "cem";
    case 200: return "duzentos";
    case 300: return "trezendos";
    case 400: return "quatrocentos";
    case 500: return "quinhentos";
    case 600: return "seiscentos";
    case 700: return "setecentos";
    case 800: return "oitocentos";
    case 900: return "novecentos";
    default: {
      var sNumero = nNumero.toString();
      var nCasasDecimais = Number(sNumero.length);
      
      switch(nCasasDecimais) {
        case 2: 
          var nDezena = Math.floor(nNumero/10);
          var nUnidade = nNumero - nDezena * 10;
          return fnExtenso(nDezena * 10) + ' e ' + fnExtenso(nUnidade);
        case 3:
          var nCentena = Math.floor(nNumero/100);
          var nDezenaUnidade = nNumero - (nCentena * 100);
          if( nCentena == 1 )
            return 'cento e ' + fnExtenso(nDezenaUnidade);
          return fnExtenso(nCentena*100) + ' e ' + fnExtenso(nDezenaUnidade);
        case 4: case 5: case 6:
          var nMilhar = Math.floor(nNumero / 1000);
          var nCentena = nNumero - (nMilhar * 1000);
          return fnExtenso(nMilhar) + ' mil' + ((nCentena > 0) ? ' ' + fnExtenso(nCentena) : '');
        case 7: case 8: case 9:
          var nMilhoes = Math.floor(nNumero / 1000000);
          var nMilhar = nNumero - (nMilhoes * 1000000);
          return fnExtenso(nMilhoes) + ' milh' + ((nMilhoes == 1) ? 'ao' :  'oes') + ((nMilhar > 0) ? ' ' + fnExtenso(nMilhar) : '');
        case 10: case 11: case 12:
          var nBilhoes = Math.floor(nNumero / 1000000000);
          var nMilhoes = nNumero - (nBilhoes * 1000000000);
          return fnExtenso(nBilhoes) + ' bilh' + ((nBilhoes == 1) ? 'ao' :  'oes') + ((nMilhoes > 0) ? ' ' + fnExtenso(nMilhoes) : '');        
        case 13: case 14: case 15:
          var nTrilhoes = Math.floor(nNumero / 1000000000000);
          var nBilhoes = nNumero - (nTrilhoes * 1000000000000);
          return fnExtenso(nTrilhoes) + ' trilh' + ((nTrilhoes == 1) ? 'ao' :  'oes') + ((nBilhoes > 0) ? ' ' + fnExtenso(nBilhoes) : '');
        default:
          return false;
      }
    }
  }
}
