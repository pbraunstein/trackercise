/**
 * Data that want to be represented in the BarCharts.ts bar chart must implement this interface
 */
export interface BarChartsBar {
    getHistoryId(): number;
    getWidth(): number;
    setWidth(value: number): void;
    getHeight(): number;
    setHeight(value: number): void;
    getXOffset(): number;
    setXOffset(value: number): void;
    getYOffset(): number;
    setYOffset(value: number): void;
    getDatestamp(): string;
    setDatestamp(value: string): void;
    getWidthBuffer(): number;
    getSets(): number;
}
