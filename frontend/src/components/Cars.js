import {useEffect, useState} from "react";
import {carService} from "../services/carService";
import {Car} from "./Car";
import {socketService} from "../services/socketService";

const Cars = () => {
    const [cars, setCars] = useState([]);
    const [trigger, setTrigger] = useState(null)

    useEffect(() => {
        carService.getAll().then(({data}) => setCars(data.data))
    }, [trigger]);

    useEffect(() => {
        socketInit()
    }, [])

    const socketInit = async () => {
        const {cars} = await socketService();
        const client = await cars();

        client.onopen = () => {
            console.log('Car socket was connected');
            client.send(JSON.stringify({
                action: 'subscribe_to_car_activity',
                request_id: new Date().getTime()
            }))
        }

        client.onmessage = (msg) => {
            const data = JSON.parse(msg.data);
            console.log(data);
            setTrigger(prev=>!prev)
        }
    }
    return (
        <div>
            {cars.map(car => <Car key={car.id} car={car}/>)}
        </div>
    );
};

export {Cars};