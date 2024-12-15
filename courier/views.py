from datetime import timedelta

from django.utils import timezone

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from courier.permissions import IsCourier
from order.models import OrderModel
from order.serializers import OrderSerializer


class MyDeliveredDeliveries(generics.ListAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsCourier]


    def get_queryset(self):
        return self.queryset.filter(courier=self.request.user, status='Delivered')


class StatisticsCourier(APIView):
    permission_classes = [IsAuthenticated, IsCourier]
    queryset = OrderModel.objects.all()
    fbd_filters = {
        'weekly': timedelta(days=7),
        'monthly': timedelta(days=30),
        'yearly': timedelta(days=365),
    }

    def get(self, request):
        courier = self.request.user
        orders = self.queryset.filter(courier=courier)

        fbd = request.GET.get('fbd')

        orders = self.apply_date_filter(orders, fbd)

        delivered_orders = orders.filter(status='Delivered')
        delivered_orders_count = delivered_orders.count()

        delivered_orders_total_price = sum(
            order.total_price for order in delivered_orders
        )

        total_assigned_orders = orders.count()
        total_canceled_orders = orders.filter(status='Cancelled').count()

        average_delivered_order_price = (
            delivered_orders_total_price / delivered_orders_count
            if delivered_orders_count > 0 else 0
        )
        data = {
            "data": orders,
            "total_assigned_orders": total_assigned_orders,
            "total_delivered_orders": delivered_orders_count,
            "total_canceled_orders": total_canceled_orders,
            "total_sum": delivered_orders_total_price,
            "average_delivered_order_price": round(average_delivered_order_price, 2),
            "pending_order": orders.filter(status='Completed--restaurant').first()
        }
        return Response(data=data, status=status.HTTP_200_OK)

    def apply_date_filter(self, orders, fbd: str):
        if fbd == 'today':
            start_of_today = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
            return orders.filter(created_at__gte=start_of_today)

        elif fbd in self.fbd_filters:
            return orders.filter(created_at__gte=timezone.now() - self.fbd_filters[fbd])
        return orders


class AcceptForDelivering(APIView):
    permission_classes = [IsAuthenticated, IsCourier]
    queryset = OrderModel

    def post(self, request):
        order = self.queryset.objects.filter(
            courier__id=request.user.pk).filter(status='Completed--restaurant')
        if order.exists():
            order = order.first()
            order.status='Completed--restaurant'
            order.save()
            data = OrderSerializer(order).data
            return Response(data={
                "success": True,
                "message": "Order accepted for delivery",
                "data": data
            }, status=status.HTTP_200_OK)

        return Response(data={
            "success": False,
            "message": "No pending orders found for this courier"
        }, status=status.HTTP_400_BAD_REQUEST)


class MarkAsDelivering(APIView):
    permission_classes = [IsAuthenticated, IsCourier]
    queryset = OrderModel

    def post(self, request):
        order = self.queryset.objects.filter(
            courier__id=request.user.pk).filter(status='Completed--restaurant')
        if order.exists():
            order = order.first()
            order.status='Completed--restaurant'
            order.save()
            data = OrderSerializer(order).data
            return Response(data={
                "success": True,
                "message": "Order marked as delivering",
                "data": data
            }, status=status.HTTP_200_OK)

        return Response(data={
            "success": False,
            "message": "No confirmed from restaurant orders found"
        }, status=status.HTTP_400_BAD_REQUEST)


class MarkAsDelivered(APIView):
    permission_classes = [IsAuthenticated, IsCourier]
    queryset = OrderModel


    def post(self, request):
        order = self.queryset.objects.filter(
            courier__id=request.user.pk).filter(status='Delivering')
        if order.exists():
            order = order.first()
            order.status='Delivered'
            order.save()
            data = OrderSerializer(order).data
            return Response(data={
                "success": True,
                "message": "Order marked as delivered",
                "data": data
            }, status=status.HTTP_200_OK)

        return Response(data={
            "success": False,
            "message": "No pending delivery order found for this courier"
        }, status=status.HTTP_400_BAD_REQUEST)