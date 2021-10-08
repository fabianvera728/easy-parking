import { Address } from './address';
import { Price } from './price';
/* eslint-disable @typescript-eslint/naming-convention */
export interface Parking{
    id?: number;
    owner: number;
    slug_name: string;
    description: string;
    phone_number: string;
    price: Price;
    address: Address;
    limit_image: number;
}
