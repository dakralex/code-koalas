import './assets/app.css';
import 'leaflet/dist/leaflet.css';
import accidents from '../data/processed/accidents.json';
import baseBikeLanes from '../data/processed/baseLayer.json';

import {useEffect, useState} from "react";
import {DivIcon, LatLng, LatLngBounds} from "leaflet";
import {MapContainer, Marker, Polyline} from "react-leaflet";
import coords, {maxLat, maxLongs, minLat, minLongs} from "./globals/outline.ts";

const App = () => {
    const outlineCoords = coords.map(p => new LatLng(p[1], p[0]));
    const mapBounds = new LatLngBounds(new LatLng(minLat, minLongs), new LatLng(maxLat, maxLongs));
    const centerCoords = new LatLng((minLat + maxLat) / 2, (minLongs + maxLongs) / 2);

    const [laneItems, setLaneItems] = useState([]);
    const [accidentPoints, setAccidentPoints] = useState([]);

    useEffect(() => {
        // @ts-ignore
        const items = Array.from(baseBikeLanes).map(item => {
            // @ts-ignore
            const latLngPts = item?.coos.map(pt => new LatLng(pt[1], pt[0]));
            return <Polyline positions={latLngPts} pathOptions={{color: '#dedede', fillColor: 'none'}}/>;
        });

        // @ts-ignore
        setLaneItems(items)
    }, []);

    // @ts-ignore
    useEffect(() => {
        const coords = Array.from(accidents).map(accident => {
            const coord = new LatLng(accident.lat, accident.lng);
            let severity: string, iconSize: number;

            if (accident.sev === 1) {
                severity = "critical";
                iconSize = 7;
            } else if (accident.sev === 2) {
                severity = "major";
                iconSize = 7;
            } else if (accident.sev === 3) {
                severity = "minor";
                iconSize = 5;
            }

            // @ts-ignore
            return <Marker position={coord} icon={new DivIcon({
                // @ts-ignore
                className: `custom-marker-icon-${severity}`,
                // @ts-ignore
                iconSize: [iconSize, iconSize]
            })}/>;
        });

        // @ts-ignore
        setAccidentPoints(coords)
    }, []);

    return (
        <>
            <MapContainer bounds={mapBounds} center={centerCoords} zoom={11} zoomSnap={0.25}
                          style={{width: '100%', backgroundColor: '#242424'}} preferCanvas={true}>
                <Polyline positions={outlineCoords} pathOptions={{color: '#dedede', fillColor: 'none'}} />
                {...accidentPoints}
                {...laneItems}
            </MapContainer>
        </>
    );
};

export default App;

