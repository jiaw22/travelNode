var lyft = require('node-lyft');
var defaultClient = lyft.ApiClient.instance;
//next you need to authorize API access.
//if you're only using your Client Token for non-user specific endpoints, you can add that token directly
defaultClient.authentications['Client Authentication'].accessToken = 'pMSEWY4ILNIuOU+x8DfD14XI3gDNhvEMeBe5m5Actfka8d1pS5PevuietivBuEg+ZxGdzL0i8OKvPTSF4SyvIpeESwaPmAxSHDYijcNpYZv0TNFcoSXU0sY=';
defaultClient.authentications['User Authentication'].accessToken = 'pMSEWY4ILNIuOU+x8DfD14XI3gDNhvEMeBe5m5Actfka8d1pS5PevuietivBuEg+ZxGdzL0i8OKvPTSF4SyvIpeESwaPmAxSHDYijcNpYZv0TNFcoSXU0sY=';
//create a new lyft-node PublicApi() instance
var lyftPublicApi = new lyft.PublicApi();
//the getETA endpoint works with both user and non-user context:
//leaving the options field empty {}
//and using promises/then to print out result
function useAPI (opts){
  lyftPublicApi.getCost(43.776841, (-79.259237),opts).then((data) => {
    var costEstimates = data.cost_estimates;
    cost = costEstimates[0].estimated_cost_cents_min;
    time = costEstimates[0].estimated_duration_seconds;
    console.log(cost+' '+time);
    return {cost: cost, time:time};
  }, (error) => {
    console.error(error);
    return {cost: -2, time:-2};
  });
};

function findCostAndDistance (startLong, startLat, endLong, endLat){
  var cost = -1;
  var time = -1 ;
  var opts = {
    'rideType':'lyft',
    'endLat': 43.547381,
    'endLng': (-79.664663)
  };
  var deferred = useAPI(opts);
    $.when(deferred).done(function() {
    console.log(deferred);
    return deferred;
  })
};


  var returnedCost = findCostAndDistance(1,1,1,1);
  console.log(returnedCost.cost +'afterthe');
