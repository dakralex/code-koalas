L.GLMarker = L.Class.extend({
	initialize(latLng, options = {}) {
		this._latLng = L.latLng(latLng);
		L.Util.setOptions(this, options);
	},
});
