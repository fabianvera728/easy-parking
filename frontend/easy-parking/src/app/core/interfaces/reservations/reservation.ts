/* eslint-disable @typescript-eslint/naming-convention */
export interface Reservation{
    id?: number;
    vehicle: number;
    parking: string;
    create_at: string;
    update_at: string;
    start_timestamp: string;
    final_timestamp: string;
    is_reserved: boolean;
    is_active: boolean;
    net_cost: number;
    is_paid: number;
    description: string;
}
