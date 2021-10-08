/* eslint-disable @typescript-eslint/naming-convention */
export interface Place{
    type: number;
    status: boolean;
    parking: number;
    description?: string;
    used_places: number;
    remaining_places: number;
    reserved_limit: number;
}
