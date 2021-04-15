#Un comerciante, el cual tiene un sueldo base, recibe un 10% extra por comisión por cada venta que realiza. Realizar un programa que devuelva el dinero que recibirá por comisión luego de 4 ventas y el total de dinero que ganará ese mes, teniendo en cuenta estas ventas y su sueldo basedef ventas(sueldo_base, dinero_venta, ventas):
def ventas(sueldo_base, dinero_venta, ventas):
    total_venta = dinero_venta * ventas
    total_comision = total_venta * 0.10
    total_mes = sueldo_base + total_comision + total_venta
    print("total comision=", str(int(total_comision)))
    print("total mes=", str(int(total_mes)))
ventas(1000, 200, 4) 